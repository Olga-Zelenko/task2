class ListValueElement:
    @staticmethod
    def get_list_value_elem_class(instance) -> list:
        """Возвращает список значений аргументов экземпляра любого класса"""
        return list(map(str, list(instance.__dict__.values())))
