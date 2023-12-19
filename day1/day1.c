#define _GNU_SOURCE
#include <assert.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int char_to_int(char *c)
{
    assert(isdigit(*c));
    int num;
    if (*c == '1')
    {
        num = 1;
    }
    else if (*c == '2')
    {
        num = 2;
    }
    else if (*c == '3')
    {
        num = 3;
    }
    else if (*c == '4')
    {
        num = 4;
    }
    else if (*c == '5')
    {
        num = 5;
    }
    else if (*c == '6')
    {
        num = 6;
    }
    else if (*c == '7')
    {
        num = 7;
    }
    else if (*c == '8')
    {
        num = 8;
    }
    else if (*c == '9')
    {
        num = 9;
    }
    return num;
}

char word_to_char(char *word)
{
    char num;
    if (!strcmp(word, "one"))
    {
        num = '1';
    }
    else if (!strcmp(word, "two"))
    {
        num = '2';
    }
    else if (!strcmp(word, "three"))
    {
        num = '3';
    }
    else if (!strcmp(word, "four"))
    {
        num = '4';
    }
    else if (!strcmp(word, "five"))
    {
        num = '5';
    }
    else if (!strcmp(word, "six"))
    {
        num = '6';
    }
    else if (!strcmp(word, "seven"))
    {
        num = '7';
    }
    else if (!strcmp(word, "eight"))
    {
        num = '8';
    }
    else if (!strcmp(word, "nine"))
    {
        num = '9';
    }
    return num;
}

int startswith(const char *pre, const char *str)
{
    return strncmp(pre, str, strlen(pre)) == 0;
}

int part1(FILE *in)
{
    int sum = 0;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    while ((read = getline(&line, &len, in)) != -1)
    {
        char digits[len];
        int k = 0;
        int line_len = strlen(line);
        for (int i = 0; i < line_len; i++)
        {
            if (isdigit(line[i]))
            {
                digits[k] = line[i];
                k++;
            }
        }
        if (k)
        {
            int first = char_to_int(&digits[0]);
            int last = char_to_int(&digits[k-1]);
            sum += first * 10 + last;
        }
    }

    return sum;
}

int part2(FILE *in)
{
    int sum = 0;
    char *line = NULL;
    char *nums[9] = {"one", "two", "three", "four", "five", "six", "seven",
                     "eight", "nine"};
    size_t len = 0;
    ssize_t read;

    while ((read = getline(&line, &len, in)) != -1)
    {
        char digits[len];
        int k = 0;
        int line_len = strlen(line);
        for (int i = 0; i < line_len; i++)
        {
            if (isdigit(line[i]))
            {
                digits[k] = line[i];
                k++;
            }
            else
            {
                char *substring = &line[i];
                for (int j = 0; j < 9; j++)
                {
                    if (startswith(nums[j], substring))
                    {
                        digits[k] = word_to_char(nums[j]);
                        k++;
                        break;
                    }
                }
            }
        }
        if (k)
        {
            int first = char_to_int(&digits[0]);
            int last = char_to_int(&digits[k-1]);
            sum += first * 10 + last;
        }
    }

    return sum;
}

int main(int argc, char *argv[])
{
    FILE *in;
    int p1;
    int p2;

    if (argc != 2)
    {
        (void)fprintf(stderr, "Usage: ./day1 [input]\n");
        exit(EXIT_FAILURE);
    }

    in = fopen(argv[1], "r");
    if (in == NULL)
    {
        (void)fprintf(stderr, "Could not open file %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    p1 = part1(in);
    rewind(in);
    p2 = part2(in);

    (void)fclose(in);

    (void)printf("Part 1: %d\n", p1);
    (void)printf("Part 2: %d\n", p2);

    /* TESTING */

    return 0;
}