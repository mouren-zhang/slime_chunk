import java.util.Random;
import java.util.*;
import java.io.*;

public class slimepk {
    public static void main(String[] args) throws Exception {
        //*�������ļ�
        //ini�ļ��Ĵ��λ��
        String filepath = "./src/config.ini";
        //�����ļ�������
        FileInputStream fis = new FileInputStream(filepath);
        //�����ļ������
        //OutputStream opt = null;
        //����Properties���Զ�����������ini�ļ��е�����
        Properties pps = new Properties();
        //���ļ����м�������
        pps.load(fis);
        //ͨ��getProperty("������")��ȡkey��Ӧ��ֵ����ֵ
        long seed = Long.parseLong(pps.getProperty("seed"));
        int x = Integer.parseInt(pps.getProperty("xs"));
        int z = Integer.parseInt(pps.getProperty("zs"));
        int x_max = Integer.parseInt(pps.getProperty("xm"));
        int z_max = Integer.parseInt(pps.getProperty("zm"));

        //*�����ʽ��
        //x��Сֵ
        x = x / 16;
        if (x < 0) {
            x--;
        }
        //z��Сֵ
        z = z / 16;
        if (z < 0) {
            z--;
        }
        //x���ֵ
        x_max = x_max / 16;
        if (x_max < 0) {
            x_max--;
        }
        //z���ֵ
        z_max = z_max / 16;
        if (z_max < 0) {
            z_max--;
        }


        //*��������
        //ʷ��ķ��������
        int yes = 0;
        //z������ֹͣ����
        int z_stop = z;
        //����ָ������ķ�Χ����12*12�������ж���
        int ax = 12;
        int az = 12;

        //���ڿ��ƿ���̨�����Ƶ��
        //ͳ��ֵ
        int pr_a = 0;
        //Ƶ��(ÿ����x�ο���̨���1��)
        int pr_stop = 500;

        //���������Ϣ
        System.out.println("0,0,0,�汾,����,����,����˵��");
        System.out.println("0,0,0,'2.0,[bilibili]ĳ��-��,'" + seed+",��������ɼ�ʱ����");



         //csv�ļ��Ƿ����
        File file = new File("Slime.csv");
        int i = 1;
        while (file.exists() ) {
            file = new File("Slime" + i + ".csv");
            i++;
        }


//        ��csv�ļ�
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
//                д���ļ�
                out.write(x * 16 + "," + z * 16 + "," + yes+"\r\n");
                //��ʱ���һ���������ֹ�û���Ϊ�ű�����
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
//        �ر��ļ�
        out.close();

    }
}
