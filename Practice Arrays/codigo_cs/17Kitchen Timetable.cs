using System;
using System.Linq;

public class Test17
{
    public static void KitchenTimetable()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int[] b = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int count = 0;
            int start = 0;
            for (int i = 0; i < n; i++)
            {
                int end = a[i];
                int dist = end - start;
                if (b[i] <= dist) count++;
                start = end;
            }
            Console.WriteLine(count);
        }
    }
}
