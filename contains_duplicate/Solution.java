import java.util.Arrays;
public class Solution
{
    public boolean containsDuplicate(int[] nums)
    {
        Arrays.sort(nums);
        int length = nums.length;
        for (int i = 1; i < length; ++i)
        {
            if (nums[i] == nums[i-1])
            {
                return true;
            }
        }
        return false;
    }
}
