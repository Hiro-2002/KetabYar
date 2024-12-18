from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'category',
            'ISBN',
            'publisher',
            'pages',
            'copies',
            'qr_code',
            'publish_date',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'qr_code', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Create the Book instance
        book = Book(**validated_data)
        # Generate the QR code
        book.generate_qr_code()
        # Save the instance with the generated QR code
        book.save()
        return book

    def update(self, instance, validated_data):
        # Update the instance fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        # Regenerate the QR code if required
        if 'qr_code' not in validated_data:
            instance.generate_qr_code()
        # Save the instance
        instance.save()
        return instance
