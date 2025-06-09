using System;

public class Test1
{
    public static void Race400M()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            string[] names = { "ALICE", "BOB", "CHARLIE" };
            int min_index = 0;
            for (int j = 0; j < arr.Length; j++)
            {
                if (arr[j] < arr[min_index])
                {
                    min_index = j;
                }
            }
            Console.WriteLine(names[min_index]);
        }
    }
}
