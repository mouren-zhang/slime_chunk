// gb2312
import java.util.Random;
import java.util.*;
import java.io.*;
import java.io.File;
//           ?下面这一行的【slimepk】一定要与文件名一致
public class slimepk {
    public static void main(String[] args) throws Exception{

        File file = new File("Slime.csv");
        int i = 1;

        while (file.exists() == true) {
            file = new File("Slime" + i + ".csv");
            if(file.exists() == true){
                i++;
            }
        }

        File f = new File("Slime" + i + ".csv");
        f.createNewFile();
        FileOutputStream fileOutputStream = new FileOutputStream(f);
        PrintStream PrintStream = new PrintStream(fileOutputStream);
        System.setOut(PrintStream);

        Scanner input = new Scanner(System.in);

        // System.out.println("地图种子：");
        long seed =input.nextLong();
        // System.out.println("X轴最小坐标：");
        int x =input.nextInt();
        x=x/16;
        if (x<0){
            x--;
        }
        // System.out.println("Z轴最小坐标：");
        int z=input.nextInt();
        z=z/16;
        if (z<0){
            z--;
        }
        // System.out.println("X轴最大坐标：");
        int x_max =input.nextInt();
        x_max=x_max/16;
        if (x_max<0){
            x_max--;
        }
        // System.out.println("Z轴最大坐标：");
        int z_max =input.nextInt();
        z_max=z_max/16;
        if (z_max<0){
            z_max--;
        }

        // if (x=="" && z=="" && x_max=="" && z_max==""){
        //     x = -23700;
        //     z = -23700;
        //     x_max = 23700;
        //     z_max = 23700;
        // }

        int yes=0;
        int z_stop = z;
        int yes_max = 0;
        int yes_max_x=0;
        int yes_max_z=0;


        //这里指定输出的范围例如8*8的区块有多少
        int ax = 8;
        int az = 8;



        System.out.println(",,,,,版本1.0,by：bilibili[mouren_zhang],查询的种子为(不包括后面的#号),"+seed+"#");
        System.out.println(",,,,,如果区域只有2-7个是不输出的");
        while (x<=x_max){
            while (z<=z_max){
                for (int a=0;a<ax;a++){
                    for (int b=0;b<az;b++){
                        Random rnd = new Random(
                                seed +
                                        (int) (x * x * 0x4c1906) +
                                        (int) (x * 0x5ac0db) +
                                        (int) (z * z) * 0x4307a7L +
                                        (int) (z * 0x5f24f) ^ 0x3ad8025f
                        );
                        if ((rnd.nextInt(10) == 0)){
                            yes++;
                        }
                        z++;
                    }
                    x++;
                    z=z-az;
                }
                x=x-ax;
                if (yes<2||yes>7){
                    System.out.println(x*16+","+z*16+",有,"+yes);
                }
                yes = 0;
                z++;
            }
            x++;
            z=z_stop;
        }
    }
}
