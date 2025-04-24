using System;
using System.Linq;

public class Test6
{
	public static void HappyParticipants()
	{
		// your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int[] b = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int count = 0;
            for (int i = 0; i < n; i++)
            {
                if (b[i] <= 2 * a[i] && a[i] <= 2 * b[i])
                {
                    count++;
                }
            }
            Console.WriteLine($"count: {count}");
        }
	}
}
