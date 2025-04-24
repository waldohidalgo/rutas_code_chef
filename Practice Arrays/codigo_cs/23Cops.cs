using System;
using System.Collections.Generic;
using System.Linq;

public class Test23
{

    static int Rec(int m, int x, int y, List<int> arr)
    {
        bool[] res = Enumerable.Repeat(true, 101).ToArray();
        res[0] = false;
        arr.Sort();
        int cover = x * y;
        int end = 0;

        foreach (int i in arr)
        {
            int curr_s = Math.Max(i - cover, 1);
            int curr_e = Math.Min(i + cover, 100);
            int start = Math.Max(curr_s, end + 1);

            for (int j = start; j <= curr_e; j++)
            {
                res[j] = false;
            }

            end = curr_e;
        }

        return res.Count(b => b);
    }
    public static void Cops()

    {
        // your code goes here


        int t = int.Parse(Console.ReadLine());
        for (int test = 0; test < t; test++)
        {
            int[] input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int m = input[0], x = input[1], y = input[2];
            List<int> arr = Console.ReadLine().Split().Select(int.Parse).ToList();

            Console.WriteLine(Rec(m, x, y, arr));
        }

    }
}
