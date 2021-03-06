/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication;

/**
 *
 * @author MarcosATSF-DESKTOP
 */
public class VirtualMachine extends javax.swing.JFrame {

    /**
     * Creates new form VirtualMachine
     */
    public VirtualMachine() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        pTab = new javax.swing.JTabbedPane();
        jScrollPane2 = new javax.swing.JScrollPane();
        jTextArea2 = new javax.swing.JTextArea();
        tabVM = new javax.swing.JPanel();
        pInstrucoes = new javax.swing.JPanel();
        jScrollPane3 = new javax.swing.JScrollPane();
        tableInstrucoes = new javax.swing.JTable();
        pPilha = new javax.swing.JPanel();
        jScrollPane4 = new javax.swing.JScrollPane();
        tablePilha = new javax.swing.JTable();
        pTerminal = new javax.swing.JPanel();
        btnNext = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        textTerminal = new javax.swing.JTextArea();
        btnRun = new javax.swing.JButton();
        menu = new javax.swing.JMenuBar();
        mArquivo = new javax.swing.JMenu();
        mEditar = new javax.swing.JMenu();
        mExecutar = new javax.swing.JMenu();
        mDebug = new javax.swing.JMenu();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jTextArea2.setColumns(20);
        jTextArea2.setRows(5);
        jScrollPane2.setViewportView(jTextArea2);

        pTab.addTab("Editor de Texto", jScrollPane2);

        pInstrucoes.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createBevelBorder(0), "Instruções"));

        tableInstrucoes.setFont(tableInstrucoes.getFont());
        tableInstrucoes.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null},
                {null, null, null, null, null}
            },
            new String [] {
                "I", "Instrução", "Param #1", "Param #2", "Comentário"
            }
        ) {
            Class[] types = new Class [] {
                java.lang.Integer.class, java.lang.String.class, java.lang.String.class, java.lang.String.class, java.lang.String.class
            };
            boolean[] canEdit = new boolean [] {
                false, false, false, false, false
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        tableInstrucoes.setAutoResizeMode(javax.swing.JTable.AUTO_RESIZE_LAST_COLUMN);
        tableInstrucoes.setMinimumSize(new java.awt.Dimension(390, 64));
        jScrollPane3.setViewportView(tableInstrucoes);
        if (tableInstrucoes.getColumnModel().getColumnCount() > 0) {
            tableInstrucoes.getColumnModel().getColumn(0).setResizable(false);
            tableInstrucoes.getColumnModel().getColumn(0).setPreferredWidth(20);
            tableInstrucoes.getColumnModel().getColumn(1).setResizable(false);
            tableInstrucoes.getColumnModel().getColumn(1).setPreferredWidth(30);
            tableInstrucoes.getColumnModel().getColumn(2).setResizable(false);
            tableInstrucoes.getColumnModel().getColumn(2).setPreferredWidth(20);
            tableInstrucoes.getColumnModel().getColumn(3).setResizable(false);
            tableInstrucoes.getColumnModel().getColumn(3).setPreferredWidth(20);
            tableInstrucoes.getColumnModel().getColumn(4).setPreferredWidth(300);
        }

        javax.swing.GroupLayout pInstrucoesLayout = new javax.swing.GroupLayout(pInstrucoes);
        pInstrucoes.setLayout(pInstrucoesLayout);
        pInstrucoesLayout.setHorizontalGroup(
            pInstrucoesLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pInstrucoesLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jScrollPane3, javax.swing.GroupLayout.DEFAULT_SIZE, 603, Short.MAX_VALUE)
                .addContainerGap())
        );
        pInstrucoesLayout.setVerticalGroup(
            pInstrucoesLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pInstrucoesLayout.createSequentialGroup()
                .addComponent(jScrollPane3, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                .addContainerGap())
        );

        pPilha.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createBevelBorder(0), "Pilha"));

        tablePilha.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null},
                {null, null},
                {null, null},
                {null, null}
            },
            new String [] {
                "Endereço [S]", "Valor"
            }
        ) {
            Class[] types = new Class [] {
                java.lang.Integer.class, java.lang.Integer.class
            };
            boolean[] canEdit = new boolean [] {
                false, true
            };

            public Class getColumnClass(int columnIndex) {
                return types [columnIndex];
            }

            public boolean isCellEditable(int rowIndex, int columnIndex) {
                return canEdit [columnIndex];
            }
        });
        tablePilha.setUpdateSelectionOnSort(false);
        jScrollPane4.setViewportView(tablePilha);
        if (tablePilha.getColumnModel().getColumnCount() > 0) {
            tablePilha.getColumnModel().getColumn(0).setResizable(false);
        }

        javax.swing.GroupLayout pPilhaLayout = new javax.swing.GroupLayout(pPilha);
        pPilha.setLayout(pPilhaLayout);
        pPilhaLayout.setHorizontalGroup(
            pPilhaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pPilhaLayout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jScrollPane4, javax.swing.GroupLayout.DEFAULT_SIZE, 179, Short.MAX_VALUE)
                .addContainerGap())
        );
        pPilhaLayout.setVerticalGroup(
            pPilhaLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pPilhaLayout.createSequentialGroup()
                .addComponent(jScrollPane4, javax.swing.GroupLayout.DEFAULT_SIZE, 260, Short.MAX_VALUE)
                .addGap(18, 18, 18))
        );

        javax.swing.GroupLayout tabVMLayout = new javax.swing.GroupLayout(tabVM);
        tabVM.setLayout(tabVMLayout);
        tabVMLayout.setHorizontalGroup(
            tabVMLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(tabVMLayout.createSequentialGroup()
                .addComponent(pInstrucoes, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGap(5, 5, 5)
                .addComponent(pPilha, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );
        tabVMLayout.setVerticalGroup(
            tabVMLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(pPilha, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addComponent(pInstrucoes, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pPilha.getAccessibleContext().setAccessibleName("Pilha");

        pTab.addTab("ASM - VM", tabVM);

        btnNext.setText("jButton1");
        btnNext.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnNextActionPerformed(evt);
            }
        });

        textTerminal.setColumns(20);
        textTerminal.setRows(5);
        jScrollPane1.setViewportView(textTerminal);

        btnRun.setText("jButton1");
        btnRun.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnRunActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout pTerminalLayout = new javax.swing.GroupLayout(pTerminal);
        pTerminal.setLayout(pTerminalLayout);
        pTerminalLayout.setHorizontalGroup(
            pTerminalLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pTerminalLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pTerminalLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addComponent(btnNext, javax.swing.GroupLayout.PREFERRED_SIZE, 50, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(btnRun, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane1)
                .addContainerGap())
        );
        pTerminalLayout.setVerticalGroup(
            pTerminalLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(pTerminalLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(pTerminalLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                    .addGroup(pTerminalLayout.createSequentialGroup()
                        .addComponent(btnNext, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(btnRun, javax.swing.GroupLayout.PREFERRED_SIZE, 72, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 160, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        mArquivo.setText("Arquivo");
        menu.add(mArquivo);

        mEditar.setText("Editar");
        menu.add(mEditar);

        mExecutar.setText("Executar");
        menu.add(mExecutar);

        mDebug.setText("Debug");
        menu.add(mDebug);

        setJMenuBar(menu);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(pTab)
                    .addComponent(pTerminal, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(pTab)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(pTerminal, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap())
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnNextActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnNextActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_btnNextActionPerformed

    private void btnRunActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnRunActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_btnRunActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(VirtualMachine.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(VirtualMachine.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(VirtualMachine.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(VirtualMachine.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new VirtualMachine().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnNext;
    private javax.swing.JButton btnRun;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JScrollPane jScrollPane3;
    private javax.swing.JScrollPane jScrollPane4;
    private javax.swing.JTextArea jTextArea2;
    private javax.swing.JMenu mArquivo;
    private javax.swing.JMenu mDebug;
    private javax.swing.JMenu mEditar;
    private javax.swing.JMenu mExecutar;
    private javax.swing.JMenuBar menu;
    private javax.swing.JPanel pInstrucoes;
    private javax.swing.JPanel pPilha;
    private javax.swing.JTabbedPane pTab;
    private javax.swing.JPanel pTerminal;
    private javax.swing.JPanel tabVM;
    private javax.swing.JTable tableInstrucoes;
    private javax.swing.JTable tablePilha;
    private javax.swing.JTextArea textTerminal;
    // End of variables declaration//GEN-END:variables
}
