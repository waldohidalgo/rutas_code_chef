using System;


public class Test9
{
	public static void CompressVideo()
	{
		// your code goes here
        int t=int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++){
            int n=int.Parse(Console.ReadLine());
            int[]a=Console.ReadLine().Split().Select(int.Parse).ToArray();
            int count=1;
            for (int i = 1; i < n; i++){
                if(a[i]!=a[i-1]) count++;
            }
            Console.WriteLine("count"+count);
        }
	}
}
