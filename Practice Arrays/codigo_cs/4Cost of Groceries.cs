using System;

public class Test4
{
	public static void Groceries()
	{
		// your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            string input = Console.ReadLine();
            int n=int.Parse(input.Split()[0]);
            int x=int.Parse(input.Split()[1]);

            int[] a = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int[] b = Console.ReadLine().Split().Select(int.Parse).ToArray();

            int cost=0;
            for (int i = 0; i < n; i++){
                if (a[i]>=x){
                    cost+=b[i];
                }
            }

        }

	}
}
