using System;
using System.Collections.Generic;

public class Test3
{
    public static void MiscellaneousLinearSearch()
    {
        // your code goes here
        int n = int.Parse(Console.ReadLine());
        var set = new HashSet<Tuple<int, int>>();

        for (int i = 0; i < n; i++)
        {
            string[] parts = Console.ReadLine().Split();
            int a = int.Parse(parts[0]);
            int b = int.Parse(parts[1]);
            set.Add(Tuple.Create(a, b));
        }
        string[] pq = Console.ReadLine().Split();
        int p = int.Parse(pq[0]);
        int q = int.Parse(pq[1]);
        if (set.Contains(Tuple.Create(p, q)) || set.Contains(Tuple.Create(q, p)))
        {
            Console.WriteLine("Yes");
        }
        else
        {
            Console.WriteLine("No");
        }
    }
}
