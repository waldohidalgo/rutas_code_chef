using System;
using System.Linq;
using System.Collections.Generic;

public class Test14
{
    public static void SocialNetwork()
    {


        var tokens = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int n = tokens[0], m = tokens[1];

        // Leer best_friends como conjunto
        var bestFriends = new HashSet<int>(
            Console.ReadLine().Split().Select(int.Parse)
        );

        // Listas para amigos y no-amigos
        var friends = new List<(int priority, string sentence)>();
        var others = new List<(int priority, string sentence)>();

        for (int i = 0; i < m; i++)
        {
            string[] parts = Console.ReadLine().Split();
            int f = int.Parse(parts[0]);
            int p = int.Parse(parts[1]);
            string s = parts[2];


            if (bestFriends.Contains(f))
            {
                friends.Add((-p, s));
            }
            else
            {
                others.Add((-p, s));
            }
        }

        friends.Sort();
        others.Sort();

        foreach (var item in friends)
        {
            Console.WriteLine(item.sentence);
        }

        foreach (var item in others)
        {
            Console.WriteLine(item.sentence);
        }

    }
}
