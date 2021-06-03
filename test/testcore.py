# from jengine.core.data import Data
# import math
# import unittest
from operator import add, mul, sub

# from jengine.core.operation import OperationCompose
# from jengine.core.network import NetworkCompose

# #
# def Sum(c, d, **kwargs):
#     return Data(c.GetData() + d.GetData())


# class TestCore(unittest.TestCase):
#     def test_sum(self):
#         """bind operation function"""

#         op_sum = OperationCompose(name="op_sum", needs=["a", "b"], provides=["sum_ab"])(
#             add
#         )

#         self.assertEqual(op_sum(1, 2), 3)

#     def test_decorator(self):
#         """decorator compute function"""

#         @OperationCompose(
#             name="op_mul",
#             needs=["sum_ab", "b"],
#             provides=["sum_ab_times_b"],
#         )
#         def op_mul(a, b):
#             return a * b

#         self.assertEqual(op_mul(2, 2), 4)

#     def test_lateBind(self):
#         """partial bind operation function"""

#         op_partial = OperationCompose(
#             name="op_partial",
#             needs=["sum_ab_p1", "sum_ab_p2"],
#             provides=["p1_plus_p2"],
#         )

#         op = op_partial(add)
#         self.assertEqual(op(5, 6), 11)

#     # def test_earlyBind(self):
#     #     """early binding function"""

#     #     op = OperationConstructor(add)

#     #     op_sum = op(name="sum_op3", needs=["a", "b"], provides="sum_ab2")

#     #     self.assertEqual(op_sum(6, 6), 12)

#     def test_param(self):
#         """param test compute function"""

#         @OperationCompose(
#             name="op_pow",
#             needs=["ab"],
#             provides=["ab_p0", "ab_p1", "ab_p2", "ab_p3"],
#             params={"exponent": 3},
#         )
#         def op_pow(a, exponent=2):
#             return [math.pow(a, y) for y in range(0, exponent + 1)]

#         result = op_pow.Compute({"ab": 2})

#         self.assertIn("ab_p0", result)
#         self.assertIn("ab_p1", result)
#         self.assertIn("ab_p2", result)
#         self.assertIn("ab_p3", result)

#         self.assertEqual(result["ab_p0"], 1)
#         self.assertEqual(result["ab_p1"], 2)
#         self.assertEqual(result["ab_p2"], 4)
#         self.assertEqual(result["ab_p3"], 8)

#     def test_compose(self):

#         op_sum = OperationCompose(name="op_sum", needs=["a", "b"], provides=["sum_ab"])(
#             add
#         )

#         @OperationCompose(
#             name="op_mul",
#             needs=["sum_ab", "b"],
#             provides=["sum_ab_times_b"],
#         )
#         def op_mul(a, b):
#             return a * b

#         @OperationCompose(
#             name="op_pow",
#             needs=["sum_ab"],
#             provides=["sum_ab_p1", "sum_ab_p2", "sum_ab_p3"],
#             params={"exponent": 3},
#         )
#         def op_pow(a, exponent=2):
#             return [math.pow(a, y) for y in range(1, exponent + 1)]

#         op_partial = OperationCompose(
#             name="op_sum_partial",
#             needs=["sum_ab_p1", "sum_ab_p2"],
#             provides=["p1_plus_p2"],
#         )
#         op_sum_partial = op_partial(add)

#         op_factory = OperationCompose(fn=add)
#         op_sum_factory = op_factory(
#             name="op_sum_early", needs=["a", "b"], provides="sum_ab2"
#         )

#         net = NetworkCompose(name="my network")(
#             op_sum, op_mul, op_pow, op_sum_partial, op_sum_factory
#         )

#         result = net({"a": 1, "b": 2})
#         check = {
#             "a": 1,
#             "b": 2,
#             "p1_plus_p2": 12.0,
#             "sum_ab": 3,
#             "sum_ab2": 3,
#             "sum_ab_p1": 3.0,
#             "sum_ab_p2": 9.0,
#             "sum_ab_p3": 27.0,
#             "sum_ab_times_b": 6,
#         }
#         self.assertEqual(result, check)

#     def test_plot(self):
#         """test plot pdf and png"""

#         def abspow(a, p):
#             return abs(a) ** p

#         # Compose the mul, sub, and abspow operations into a computation graph.
#         net = NetworkCompose(name="graph")(
#             OperationCompose(name="mul1", needs=["a", "b"], provides=["ab"])(mul),
#             OperationCompose(name="sub1", needs=["a", "ab"], provides=["a_minus_ab"])(
#                 sub
#             ),
#             OperationCompose(
#                 name="abspow1",
#                 needs=["a_minus_ab"],
#                 provides=["abs_a_minus_ab_cubed"],
#                 params={"p": 3},
#             )(abspow),
#         )

#         net.Plot()

#     def test_factory(self):
#         """create operation class object"""

#         registry = {"add": Sum}

#         op_sum_factory = OperationCompose(
#             name="sum1",
#             needs=["a", "b"],
#             provides=["sum_ab2"],
#             params={"exponent": 3},
#         )
#         op_factory0 = op_sum_factory(registry.get("add"))

#         op_sum_factory1 = OperationCompose(
#             name="sum2",
#             needs=["sum_ab2", "d"],
#             provides=["sum_ab3"],
#             params={"exponent": 4},
#         )
#         op_factory1 = op_sum_factory1(registry.get("add"))

#         net = NetworkCompose(name="graph")(op_factory0, op_factory1)
#         print(
#             net(
#                 {
#                     "a": Data(1),
#                     "b": Data(1),
#                     "sum_ab2": Data(2),
#                     "d": Data(3),
#                 }
#             )
#         )
#         # net.Plot()
