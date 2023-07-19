from delivery_company.models import Drone, Medication, Order, LoadItem
from rest_framework import serializers
from delivery_company.validators import validate_drone_weight_limit


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ('serial_number',
                  'drone_model',
                  'weight_limit',
                  'battery_capacity',
                  'state', )

    def validate(self, data):
        quantity_of_drones = Drone.objects.count()
        if quantity_of_drones >= 10:
            raise serializers.ValidationError(f"Company only have 10 drones, "
                                              f"actual number of drones {quantity_of_drones}")
        drone_model = data['drone_model']
        weight_limit = data['weight_limit']
        validate_drone_weight_limit(drone_model, weight_limit)
        return data


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ('code', 'name', 'weight', 'image', )


class LoadItemSerializer(serializers.ModelSerializer):
    medication = MedicationSerializer()

    class Meta:
        model = LoadItem
        fields = ('medication', 'quantity',)


class OrderSerializer(serializers.ModelSerializer):
    drone = DroneSerializer()
    items = LoadItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('order_code', 'drone', 'date')
        read_only_fields = ('date', )
        extra_kwargs = {'items': {'write_only': True}}

    @staticmethod
    def validation_rules(drone, items):
        total = 0
        for medication_and_quantity in items:
            medication = medication_and_quantity.get('medication')
            quantity = medication_and_quantity.get('quantity')
            total += medication.weight * quantity
        if total > drone.weight_limit:
            raise serializers.ValidationError(f"This drone has a load limit of {drone.weight_limit} g "
                                              f"and the load to be sent {total} g exceeds that limit")
        if drone.state != "IDL":
            raise serializers.ValidationError(f"The drone {drone.serial_number} can't be loaded, "
                                              f"actual state of  this drone {drone.state}")
        if drone.battery_capacity < 25:
            raise serializers.ValidationError(f"The battery of this drone is {drone.battery_capacity}, "
                                              f"a drone can't fly if its battery is below 25 %")

    def validate(self, data):
        drone = data['drone']
        items = data['items']
        self.validation_rules(drone=drone, items=items)
        return data

    def create(self, validated_data):
        order_code = validated_data.get('order_code')
        drone = validated_data.get('drone')
        items = validated_data.get('items')
        # The new order is created
        new_order = Order.objects.create(order_code=order_code, drone=drone, )
        # Logic to create the items of the previously created order
        items_list = []
        for medication_and_quantity in items:
            medication = medication_and_quantity.get('medication')
            quantity = medication_and_quantity.get('quantity')
            new_item = LoadItem(order_code=new_order, medication=medication, quantity=quantity)
            items_list.append(new_item)
        save_items = LoadItem.objects.bulk_create(items_list)
        # Change the state of the drone from IDLE to LOADED, to specify that this drone is loaded
        drone.state = "LDD"
        drone.save()
        return new_order

