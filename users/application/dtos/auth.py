from abc import ABC

from rest_framework import serializers


class PhoneNumberRequestDTO(serializers.Serializer, ABC):
    """
    public class PhoneNumberRequestModel
    {
        [Required]
        [DataType(DataType.PhoneNumber)]
        public string Phone { get; set; }
    }
    """

    phone = serializers.CharField()


class VerifyCodeDTO(serializers.Serializer, ABC):
    code = serializers.CharField()
    phone = serializers.CharField()


class RegisterDTO(serializers.Serializer, ABC):
    """
    [DataType(DataType.EmailAddress)]
    public string Email { get; set; }
    [Required]
    public string Password { get; set; }
    [Required]
    public string Name { get; set; }
    [Required]
    public string Nickname { get; set; }
    [Required]
    [DataType(DataType.PhoneNumber)]
    public string Phone { get; set; }
    """

    email = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    nickname = serializers.CharField()
    phone = serializers.CharField()


class LoginDTO(serializers.Serializer, ABC):
    id = serializers.CharField()
    password = serializers.CharField()
