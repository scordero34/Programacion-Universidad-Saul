/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.clase2;

import javax.swing.JOptionPane;

/**
 *
 * @author User
 */
public class Programa_Salario_Trabajador {

    public static void main(String[] args) {

        String SnombreTrabajador = JOptionPane.showInputDialog(
                "Digite el nombre del trabajador");

        String SsalarioSemanal = JOptionPane.showInputDialog(
                "Digite el salario semanal");

        double NsalarioSemanal;
        double NsalarioBruto;
        double Ndeducciones;
        double NsalarioNeto;

        NsalarioSemanal = Double.parseDouble(SsalarioSemanal);

        NsalarioBruto =
                NsalarioSemanal * 4;

        Ndeducciones =
                NsalarioBruto * 0.0934;

        NsalarioNeto =
                NsalarioBruto - Ndeducciones;

        JOptionPane.showMessageDialog(null,
                "Estimado " + SnombreTrabajador
                + ", el salario de este mes se desglosa de la siguiente manera.\n\n"
                + "Salario bruto: "
                + NsalarioBruto
                + "\nDeducciones: "
                + Ndeducciones
                + "\nSalario Neto: "
                + NsalarioNeto);

    }
}

