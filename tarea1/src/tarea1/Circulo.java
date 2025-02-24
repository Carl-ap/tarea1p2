/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package tarea1;

/**
 *
 * @author Carl Ap
 */
import javax.swing.JPanel;
import java.awt.Graphics;

public class Circulo {
    private Punto centro;
    private int radio;

    public Circulo(Punto centro, int radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public void dibujarCirculo(Graphics g) {
        int x = (int) (centro.getX() - radio);
        int y = (int) (centro.getY() - radio);
        int diametro = 2 * radio;
        g.drawOval(x, y, diametro, diametro);
    }
}

