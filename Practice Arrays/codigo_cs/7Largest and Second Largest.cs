using System;

public class Test7
{
	public static void TwoLargest()
	{
		// your code goes here
		int t = int.Parse(Console.ReadLine());
		for (int _ = 0; _ < t; _++)
		{
			int n = int.Parse(Console.ReadLine());
			int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
			int max1 = 0, max2 = 0;
			for (int i = 0; i < n; i++)
			{
				if (a[i] > max1)
				{
					max2 = max1;
					max1 = a[i];
				}
				else if (a[i]!=max1 && a[i] > max2)
				{
					max2 = a[i];
				}
			}
			Console.WriteLine($"result {max1+ max2}");
		}
	}
}
