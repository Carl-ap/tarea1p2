/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tarea1;
/**
 *
 * @author Carl Ap
 */

import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.Graphics;

public class MiJFrame extends JFrame {
    private Linea linea;
    private Circulo circulo;

    public MiJFrame() {
        setTitle("Dibujo de Linea y Circulo");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Inicializar puntos, línea y círculo
        Punto p1 = new Punto(0, 300);
        Punto p2 = new Punto(400, 0);
        linea = new Linea(p1, p2);

        Punto centro = new Punto(200, 200);
        circulo = new Circulo(centro, 50); // Aquí no debería lanzarse UnsupportedOperationException

        // Agregar JPanel para dibujar
        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                linea.dibujarLinea(g);
                circulo.dibujarCirculo(g);
            }
        };

        add(panel);
    }

    public static void main(String[] args) {
        MiJFrame frame = new MiJFrame();
        frame.setVisible(true);
    }
}

