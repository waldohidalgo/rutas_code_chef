using System;

public class Test10
{
    public static void Sticks()
    {
        int t = int.Parse(Console.ReadLine());
        for (int j = 0; j < t; j++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);

            Array.Sort(arr);
            Array.Reverse(arr);
            int? s1 = null;
            int? s2 = null;
            int i = 0;
            while (i < n)
            {
                if (s1 == null && i + 1 < n && arr[i] == arr[i + 1])
                {
                    s1 = arr[i];
                    i += 2;
                }
                if (s1 != null)
                {
                    if (i + 1 < n && arr[i] == arr[i + 1])
                    {
                        s2 = arr[i];
                        break;
                    }
                }
                i++;
            }
            if (s1 != null && s2 != null)
            {
                Console.WriteLine(s1 * s2);
            }
            else
            {
                Console.WriteLine(-1);
            }

        }
    }
}
