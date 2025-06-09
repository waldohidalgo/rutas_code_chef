using System;
using System.Collections.Generic;
using System.Linq;

public class Test12
{
    public static void MaximumWeightDifference()
    {
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            var tokens = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int n = tokens[0], k = tokens[1];
            var arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

            int total = arr.Sum();

            var minHeap = new PriorityQueue<int, int>();
            foreach (var num in arr)
            {
                minHeap.Enqueue(num, num);
            }

            int group1 = 0;
            int limit = Math.Min(k, n - k);
            for (int i = 0; i < k; i++)
            {
                group1 += minHeap.Dequeue();
            }

            int group2 = total - group1;
            Console.WriteLine(Math.Abs(group2 - group1));
        }
    }
}
