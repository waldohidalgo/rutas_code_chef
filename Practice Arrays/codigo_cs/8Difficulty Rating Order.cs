using System;

public class Test8
{
	public static void CheckOrderDifficulty()
	{
		// your code goes here
        int t=int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++){
            int n=int.Parse(Console.ReadLine());
            int[]d=Console.ReadLine().Split().Select(int.Parse).ToArray();
            bool flag=false;
            for (int i = 1; i < n; i++){
                if (d[i-1]>d[i]){
                    Console.WriteLine("No");
                    flag=true;
                    break;
                }
            }
            
            if (!flag) Console.WriteLine("Yes");}
	}
}
