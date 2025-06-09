using System;

public class Test11
{
    public static void Meatballs()
    {
        int t = int.Parse(Console.ReadLine());
        for (int j = 0; j < t; j++)
        {
            string input = Console.ReadLine();
            int n = int.Parse(input.Split(' ')[0]);
            int m = int.Parse(input.Split(' ')[1]);
            int[] p = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            Array.Sort(p);
            Array.Reverse(p);
            int count_plates = 0;
            int count_meatballs = 0;
            for (int i = 0; i < n; i++)
            {
                count_meatballs += p[i];
                count_plates += 1;
                if (count_meatballs >= m)
                {
                    Console.WriteLine(count_plates);
                    break;
                }
            }
            if (count_meatballs < m)
            {
                Console.WriteLine(-1);
            }


        }
    }
}
