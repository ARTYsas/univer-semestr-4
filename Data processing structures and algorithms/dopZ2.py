class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def calculate_mean(root):
    if root is None:
        return None

    stack = []
    total_sum = 0
    count = 0

    # Выполняем итеративный последовательный обход с использованием стека
    current = root
    while current or stack:
        while current:
            stack.append(current)  # Добавляем текущий узел в стек
            current = current.left  # Переходим к левому потомку

        current = stack.pop()  # Извлекаем узел из стека
        total_sum += current.val  # Добавляем значение текущего узла к общей сумме
        count += 1  # Увеличиваем счетчик узлов

        current = current.right  # Переходим к правому потомку

    return total_sum / count  # Вычисляем и возвращаем среднее арифметическое


# Проверяем реализацию
# Создаем бинарное дерево
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Вычисляем среднее арифметическое
mean = calculate_mean(root)
print("Среднее арифметическое:", mean)
