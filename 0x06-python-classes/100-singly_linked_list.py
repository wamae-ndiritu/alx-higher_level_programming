#!/usr/bin/python3


"""
Defines a Node for a singly linked list
and then defines a SinglyLinked List class to create a sll
"""


class Node:
    """
    Defines a node
    """

    def __init__(self, data, next_node=None):
        """
        Instantiates class Node

        Args:
            data (int): Data stored in the node of the list
            next_node (string): Pointer to the next node of the list
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Data getters method

        Returns:
            int: List node data
        """

        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the value of list node data

        Args:
            value (int): New value to the list node data
        Raises:
            TypeError: If value is not an integer
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """
        Gets the next_node (Getter)

        Returns:
            Node: returns reference to the next node
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next_node pointer

        Args:
            value (Node): The reference to the next node
        Raises:
            TypeError: If next_node is not None or a Node.
        """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly Linked list
    """

    def __init__(self):
        """
        Instatiates the SinglyLInkedList

        Attributes:
            __head: The private instance attribute for the head node.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list

        Args:
            value (int): The value to be inserted into the list.
        """

        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None:
                if value >= current.next_node.data:
                    current = current.next_node
                else:
                    break
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the singly linked list.

        Returns:
            str: The string representation of the list
        """

        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
