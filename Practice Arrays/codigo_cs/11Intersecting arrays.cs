using System;
using System.Collections.Generic;
using System.Linq;

public class Test11
{

    static List<int> Intersect(int[] nums1, int[] nums2)
    {
        Dictionary<int, int> ct1 = new Dictionary<int, int>();
        Dictionary<int, int> ct2 = new Dictionary<int, int>();

        foreach (int num in nums1)
        {
            if (ct1.TryGetValue(num, out int count))
            {
                ct1[num] = count + 1;
            }
            else
            {
                ct1[num] = 1;
            }
        }

        foreach (int num in nums2)
        {
            if (ct2.TryGetValue(num, out int count))
                ct2[num] = count + 1;
            else
                ct2[num] = 1;
        }

        List<int> res = new List<int>();

        for (int i = 0; i <= 100; i++)
        {
            if (ct1.TryGetValue(i, out int value1) && ct2.TryGetValue(i, out int value2))
            {
                int times = Math.Min(value1, value2);
                for (int j = 0; j < times; j++)
                {
                    res.Add(i);
                }
            }
        }

        return res;
    }
    public static void IntersectingArrays()
    {
        int[] sizes = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int[] nums1 = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int[] nums2 = Console.ReadLine().Split().Select(int.Parse).ToArray();

        List<int> ans = Intersect(nums1, nums2);
        Console.WriteLine(string.Join(" ", ans));

    }
}
