public class Solution
{
    /*
        I think there must be this precondition:
        The input array is not empty.
    */
    public int[] plusOne(int[] digits)
    {
        int j = 0;
        int length = digits.length;
        int lenOfNinePart = 0;
        while (j < length)
        {
            if (digits[j] != 9)
            {
                lenOfNinePart = j;
                break;
            }
            ++j;
        }
        int[] result;
        if (j == length)
        {
            lenOfNinePart = length;
            result = new int[length+1];
            result[0] = 1;
            for (int i = 1; i < length + 1; ++i)
            {
                result[i] = 0;
            }
        }
        else
        {
            result = new int[length];
            int carry = 1;
            int k = length - 1;
            while (k >= lenOfNinePart)
            {
                result[k] = (digits[k] + carry) % 10;
                carry = (digits[k] + carry) / 10;
                --k;
                if (carry == 0)
                {
                    break;
                }
            }
            for (; k >= 0; --k)
            {
                result[k] = digits[k];
            }
        }
        return result;
    }
}
