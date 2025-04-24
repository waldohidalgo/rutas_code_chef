using System;
using System.Linq;
using System.Collections.Generic;
public class Test22
{
    public static void CountMaximum()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
            Dictionary<int, int> dict = new Dictionary<int, int>();
            int max_count = 0;
            int elem = 0;
            for (int i = 0; i < n; i++)
            {
                if (dict.TryGetValue(a[i], out int value))
                {
                    dict[a[i]] = ++value;
                }
                else
                {
                    dict.Add(a[i], 1);
                }

                if (dict[a[i]] > max_count)
                {
                    max_count = dict[a[i]];
                    elem = a[i];
                }
                else if (dict[a[i]] == max_count && a[i] < elem)
                {
                    elem = a[i];
                }
            }
            Console.WriteLine($"{elem} {max_count}");
        }
    }
}