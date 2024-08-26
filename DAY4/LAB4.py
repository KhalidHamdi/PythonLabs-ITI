#  q1 Class Person:
# 		attributes: name, age
# 		methods: say_hello, say_age

# class SuperHero: that inherits from person
# 		 attributes += secret_identity, nemesis
# 		 methods: reveal_secret_identity, say_hello, old_say_age, say_age



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hello(self):
#         print(f"Hello my name is {self.name}.")

#     def say_age(self):
#         print(f"I am {self.age} years old.")

# class SuperHero(Person):
#     def __init__(self, name, age, secret_identity, nemesis):
#         super().__init__(name, age)
#         self.secret_identity = secret_identity
#         self.nemesis = nemesis

#     def reveal_secret_identity(self):
#         print(f"The world knows me as a hero but I am {self.secret_identity}.")

#     def say_hello(self):
#         print(f"{self.name} at your service.")

#     def old_say_age(self):
#         super().say_age()

#     def say_age(self):
#         print(f"As a superhero I do not reveal my true age")




# ======================================================================================================================


# # 2 - A Queue is a linear structure which follows a particular order in which the operations are performed.
# # The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a
# # resource where the consumer that came first is served first.

# # We need to implement a python class that represents the queue data structure:

# # 	The class should have these operations:
# # 		- enqueue(value) => inserts a new value at the rear of the queue
# # 		- dequeue() 	 => returns and removes a value from the front of the queue.
# # 				    We should return None and print a warning message if we tried to pop value from an empty queue
# # 		- is_empty() 	 => which returns True or False to represent whether the queue is empty or not



# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, value):
#         self.queue.append(value)
#         print(f"Enqueued: {value}")

#     def dequeue(self):
#         if not self.is_empty():
#             value = self.queue.pop(0) 
#             print(f"Dequeued: {value}")
#             return value
#         else:
#             print("The queue is empty, no items to remove")
#             return None

#     def is_empty(self):
#         return len(self.queue) == 0

# ======================================================================================================================
