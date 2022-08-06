import java.util.Random;
import java.util.*;
import java.io.*;

public class slimepk {
    public static void main(String[] args) throws Exception{
        //读配置文件
        String filepath = "./src/config.ini";
        //创建文件输入流
        FileInputStream fis = new FileInputStream(filepath);
//        创建Properties属性对象用来接受ini文件中的属性
        Properties pps = new Properties();
//        从文件流中加载属性
        pps.load(fis);
        //通过getProperty("属性名")获取key对应的值并赋值

        long seed = Long.parseLong(pps.getProperty("seed"));
        int x = Integer.parseInt(pps.getProperty("x_min"));
        int z = Integer.parseInt(pps.getProperty("z_min"));
        int x_max = Integer.parseInt(pps.getProperty("x_max"));
        int z_max = Integer.parseInt(pps.getProperty("z_max"));

        //*坐标格式化
        //x最小值
        x = x / 16;
        if (x < 0) {
            x--;
        }
        //z最小值
        z = z / 16;
        if (z < 0) {
            z--;
        }
        //x最大值
        x_max = x_max / 16;
        if (x_max < 0) {
            x_max--;
        }
        //z最大值
        z_max = z_max / 16;
        if (z_max < 0) {
            z_max--;
        }

        //*其他参数
        //史莱姆区块数量
        int yes = 0;
        //z轴区域停止坐标
        int z_stop = z;
        //这里指定输出的范围例如12*12的区块有多少
        int ax = 12;
        int az = 12;

        //用于控制控制台输出的频率
        //统计值
        int pr_a = 0;
        //频率(每计算x次控制台输出1次)
        int pr_stop = 500;

        System.out.println("正在运行脚本");

        //csv文件是否存在
        File file = new File("Slime.csv");
        int i = 1;
        while (file.exists() ) {
            file = new File("Slime" + i + ".csv");
            i++;
        }


//        打开csv文件
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file,true)));






        while (x <= x_max) {
            while (z <= z_max) {
                for (int a = 0; a < ax; a++) {
                    for (int b = 0; b < az; b++) {
                        Random rnd = new Random(
                                seed +
                                        (int) (x * x * 0x4c1906) +
                                        (int) (x * 0x5ac0db) +
                                        (int) (z * z) * 0x4307a7L +
                                        (int) (z * 0x5f24f) ^ 0x3ad8025f
                        );
                        if ((rnd.nextInt(10) == 0)) {
                            yes++;
                        }
                        z++;
                    }
                    x++;
                    z = z - az;
                }
                x = x - ax;
//                写入文件
                out.write(x * 16 + "," + z * 16 + "," + yes+"\r\n");
                //定时输出一个结果，防止用户认为脚本假死
                if (pr_a >= pr_stop) {
                    System.out.println(x * 16 + "," + z * 16 + "," + yes);
                    pr_a = 0;
                }
                pr_a++;

                yes = 0;
                z++;
            }
            x++;
            z = z_stop;
        }
//        关闭文件
        out.close();



    }
}
