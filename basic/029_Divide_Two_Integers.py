class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # sign
        sign = (divisor < 0) is (dividend < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        # quotient and product
        quotient = 0
        sum_ = divisor

        # iteration
        while sum_ <= dividend:
            # initialization for each loop
            temp_quotient = 1
            while (sum_ << 1) <= dividend:
                sum_ <<= 1
                temp_quotient <<= 1
            dividend -= sum_
            quotient += temp_quotient
            # reset sum_
            sum_ = divisor

        # determine the sign
        if not sign:
            quotient = -quotient
        if quotient > 2**31 - 1:
            return 2**31 - 1

        return quotient