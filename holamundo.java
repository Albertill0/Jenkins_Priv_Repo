import java.io.*;

public class HelloWorld {
    public static void main(String[] args) {
        try {
            // Suponiendo que los datos provienen de una fuente externa
            String serializedData = args[0];
            
            // Deserializar datos sin validar o asegurar
            ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(serializedData.getBytes()));
            Object obj = ois.readObject();
            ois.close();
            
            System.out.println("Hello, World!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
