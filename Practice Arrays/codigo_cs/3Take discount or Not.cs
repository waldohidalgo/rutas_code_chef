using System;

public class Test3
{
	public static void DiscountOrNot()
	{
		// your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            string[] inputs = Console.ReadLine().Split();
            int n = int.Parse(inputs[0]);
            int x = int.Parse(inputs[1]);
            int y = int.Parse(inputs[2]);

            int[] a = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

            int totalWithoutDiscount = 0;
            int totalWithDiscount = x;

            foreach (int el in a)
            {
                totalWithoutDiscount += el;
                totalWithDiscount += (el - y) >= 0 ? (el - y) : 0;
            }

            if (totalWithDiscount < totalWithoutDiscount)
            {
                Console.WriteLine("COUPON");
            }
            else
            {
                Console.WriteLine("NO COUPON");
            }

        }
	}
}
