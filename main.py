from pydantic import BaseModel, EmailStr, ValidationError, Field, field_validator, model_validator


class Address(BaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)  # препод сказал минимум 3
    house_number: int = Field(gt=0)  # препод сказал должно быть положительным

    model_config = dict(
        str_strip_whitespace=True,
    )


class User(BaseModel):
    name: str = Field(min_length=2, pattern=r'^[a-zA-Zа-яА-ЯёЁ\s]+$')  # только буквы через Field
    age: int = Field(ge=0, le=120)  # препод сказал через Field
    email: EmailStr
    is_employed: bool
    address: Address

    model_config = dict(
        str_strip_whitespace=True,
    )

    @model_validator(mode='after')
    def check_employment_age(self):
        if self.is_employed and not (18 <= self.age <= 65):
            raise ValueError(
                f"Employed user must be between 18 and 65 years old, got {self.age}"
            )
        return self

    def __str__(self):
        return f"User {self.name}, {self.age} years old. Email: {self.email}. City: {self.address.city}"


def register_user(json_string: str):
    try:
        user = User.model_validate_json(json_string)
        print(f"Успех: {user}")
        return user.model_dump_json()
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")
        return e.json()  # препод сказал чтобы функция возвращала один тип


if __name__ == '__main__':

    json_valid = """{
        "name": "John Doe",
        "age": 25,
        "email": "john.doe@example.com",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house_number": 123
        }
    }"""

    json_age_error = """{
        "name": "John Doe",
        "age": 70,
        "email": "john.doe@example.com",
        "is_employed": true,
        "address": {
            "city": "New York",
            "street": "5th Avenue",
            "house_number": 123
        }
    }"""

    json_old_not_employed = """{
        "name": "Alice Smith",
        "age": 70,
        "email": "alice@example.com",
        "is_employed": false,
        "address": {
            "city": "Boston",
            "street": "Main Street",
            "house_number": 10
        }
    }"""

    json_bad_name = """{
        "name": "John123",
        "age": 25,
        "email": "john@example.com",
        "is_employed": false,
        "address": {
            "city": "LA",
            "street": "Sunset Blvd",
            "house_number": 5
        }
    }"""

    print("=== Тест 1 - валидный юзер ===")
    result = register_user(json_valid)
    print(result)

    print("\n=== Тест 2 - возраст не подходит ===")
    register_user(json_age_error)

    print("\n=== Тест 3 - старый но не работает ===")
    result = register_user(json_old_not_employed)
    print(result)

    print("\n=== Тест 4 - имя с цифрами ===")
    register_user(json_bad_name)