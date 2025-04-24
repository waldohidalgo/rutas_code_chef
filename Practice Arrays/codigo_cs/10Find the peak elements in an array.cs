using System;
using System.Collections.Generic;

public class Test10
{
	public static void PeaksElements()
	{
		// your code goes here
        int n=int.Parse(Console.ReadLine());
        int[]arr=Console.ReadLine().Split().Select(int.Parse).ToArray();
        int prev = 0;
        int next = n > 1 ? arr[1] : 0;

        List<int> res = new List<int>();
        for (int i = 0; i < n; i++)
        {
            if (arr[i] > prev && arr[i] > next)
            {
                res.Add(arr[i]);
            }

            prev = arr[i];
            next = (i + 2 < n) ? arr[i + 2] : 0;
        }
        if(res.Count==0){
             Console.WriteLine("-1");
        }else{
            Console.WriteLine(string.Join(" ", res));
        }


	}
}
