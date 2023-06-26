from whiteboard import solution
from unittest import TestCase, main


class WhiteboardTest(TestCase):

    def test_a(self):
        self.assertEqual(solution("foo"),"foo1")

    def test_b(self):
        self.assertEqual(solution("foobar23"),"foobar24")

    def test_c(self):
        self.assertEqual(solution("foo0042"),"foo0043")

    def test_d(self):
        self.assertEqual(solution("foo9"),"foo10")

    def test_e(self):
        self.assertEqual(solution("foo099"),"foo100")
if __name__ == '__main__':
    main()