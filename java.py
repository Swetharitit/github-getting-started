import java.util.scanner;
class Squarepattern
{
    public static void main(string[] args)
    {
        Scanner sc=new scanner(System.in);
        System.out.print("Enter n values:");
        int n=sc.nextInt();
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                System.out.print("*");
            }
            System.out.println();
        }

     }

}
