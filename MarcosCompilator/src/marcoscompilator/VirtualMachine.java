/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package marcoscompilator;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ComponentListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JTextArea;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.event.MenuEvent;
import javax.swing.event.MenuKeyEvent;
import javax.swing.event.MenuKeyListener;
import javax.swing.event.MenuListener;
import javax.swing.table.DefaultTableModel;
import javax.swing.text.AbstractDocument;
import javax.swing.text.Document;
import javax.swing.text.Element;
import javax.swing.text.DocumentFilter;
import javax.swing.text.AttributeSet;
import javax.swing.text.BadLocationException;

/**
 *
 * @author MarcosATSF-DESKTOP
 */
public class VirtualMachine extends javax.swing.JFrame {

    public static final int SLEEPING = 0;
    public static final int RUN = 1;
    public static final int RUN_DEBUG = 2;
    
    DefaultTableModel model, modelStack;
    JTextArea lines;
    Filter filterDocument;
    InterfaceVmCodigo interfaceVmCodigo;
    String valorLido;
    boolean executando;
    boolean executandoDebug;
    boolean nextInstruction;
    int stopInstruction;
    public static int state;
    
    private static VirtualMachine instance = null;
    
    public static VirtualMachine getInstance(){
        if(instance == null) instance = new VirtualMachine();
        return instance;
    }

    public VirtualMachine() {
        initComponents();
        model = (DefaultTableModel) tableInstrucoes.getModel();
        modelStack = (DefaultTableModel) tablePilha.getModel();
        valorLido = "";
        stopInstruction = -1;
        executando = false;
        executandoDebug = false;
        nextInstruction = false;
        state = SLEEPING;
    }
    
    public void addAsmRow(int i, String instrucao){
        model.addRow(new Object[]{i, instrucao, "", ""});
    }
    
    public void addAsmRow(int i, String instrucao, int param1){
        model.addRow(new Object[]{i, instrucao, param1, ""});
    }
    
    public void addAsmRow(int i, String instrucao, int param1, int param2){
        model.addRow(new Object[]{i, instrucao, param1, param2});
    }

    public void editJmpValue(int value, int row){
        model.setValueAt(value, row - 1, 2);
    }
    
    public void setComment(int row, String comment){
        model.setValueAt(comment, row - 1, 4);
    }
    
    public String getOperation(int row){
        return (String)model.getValueAt(row - 1, 1);
    }
    
    public int getParam1(int row){
        return (int)model.getValueAt(row - 1, 2);
    }
    
    public int getParam2(int row){
        return (int)model.getValueAt(row - 1, 3);
    }
    
    public void updateStack(ArrayList<Integer> m){
        for(int pos=0; pos< m.size(); pos++){
            try{
                if(modelStack.getValueAt(pos, 1) != m.get(pos)) 
                    modelStack.setValueAt(m.get(pos), pos, 1);
                else if(modelStack.getValueAt(pos, 1) == m.get(pos))
                    continue;
            }catch(ArrayIndexOutOfBoundsException err){
               modelStack.addRow(new Object[]{pos, m.get(pos)}); 
            }                
        }
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
        textCode = new javax.swing.JTextArea();
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
        mReset = new javax.swing.JMenu();
        mExecutar = new javax.swing.JMenu();
        mDebug = new javax.swing.JMenu();
        mStatus = new javax.swing.JMenu();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        textCode.setColumns(20);
        textCode.setRows(5);
        jScrollPane2.setViewportView(textCode);

        pTab.addTab("Editor de Texto", jScrollPane2);

        pInstrucoes.setBorder(javax.swing.BorderFactory.createTitledBorder(javax.swing.BorderFactory.createBevelBorder(0), "Instruções"));

        tableInstrucoes.setFont(tableInstrucoes.getFont());
        tableInstrucoes.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {},
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
        tableInstrucoes.getSelectionModel().addListSelectionListener(new ListSelectionListener() {
            @Override
            public void valueChanged(ListSelectionEvent e) {
                System.out.println(tableInstrucoes.getValueAt(tableInstrucoes.getSelectedRow(), 0).toString());
                stopInstruction = Integer.parseInt(tableInstrucoes.getValueAt(tableInstrucoes.getSelectedRow(), 0).toString())-1;
                //throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
            }
        });
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
            new Object [][] {},
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

        btnNext.setText("Nxt");
        btnNext.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnNextActionPerformed(evt);
            }
        });
        btnNext.setEnabled(false);

        
        textTerminal.setColumns(20);
        textTerminal.setRows(5);
        textTerminal.setText("");
        textTerminal.setEditable(false);
        textTerminal.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {}

            @Override
            public void keyPressed(KeyEvent e) {
                if(e.getKeyCode() == KeyEvent.VK_ENTER){
                    //Regex parsear quando for enter ou espaço =)
                    valorLido = "";
                    String[] aux = textTerminal.getText().split("Entrada: |\\r\\n|\\n|\\r");
                    for (String character : aux) {
                        valorLido += character;
                    }
                    textTerminal.setText("");
                    textTerminal.setEditable(false);
                    
                    returnValueRead();
                }
            }

            @Override
            public void keyReleased(KeyEvent e) {}
        });
        
        filterDocument = new Filter();
        ((AbstractDocument) textTerminal.getDocument()).setDocumentFilter(filterDocument);
        jScrollPane1.setViewportView(textTerminal);

        btnRun.setText("Run");
        btnRun.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnRunActionPerformed(evt);
            }
        });
        btnRun.setEnabled(false);

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

        mReset.setText("Reiniciar");
        //TODO reset program execution
        menu.add(mReset);

        mExecutar.setText("Executar");
        mExecutar.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent arg0) {
                if(!executando){
                    System.out.println("Iniciando execucao");
                    executando = true;
                    mDebug.setEnabled(false);
                    
                    runCode(RUN);
                }else{
                    System.out.println("Programa ja executando");
                }
            }
        });
        menu.add(mExecutar);

        
        mDebug.setText("Debug");
        mDebug.addChangeListener(new ChangeListener() {
            @Override
            public void stateChanged(ChangeEvent arg0) {
                if(!executandoDebug){
                    System.out.println("Iniciando execucao");
                    executandoDebug = true;
                    mExecutar.setEnabled(false);
                    
                    runCode(RUN_DEBUG);
                }else{
                    System.out.println("Programa ja executandoDebug");
                }
            }
        });
        menu.add(mDebug);
        
        mStatus.setText("");
        menu.add(mStatus);
        
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
        btnNext.setEnabled(false);
        InterfaceVmCodigo.setNxtInst(true);
        interfaceVmCodigo.runDebug(this, stopInstruction);
        // TODO add your handling code here:
    }//GEN-LAST:event_btnNextActionPerformed

    private void btnRunActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnRunActionPerformed
        btnRun.setEnabled(false);
        InterfaceVmCodigo.setNxtInst(false);
        interfaceVmCodigo.run(this);
        // TODO add your handling code here:
    }//GEN-LAST:event_btnRunActionPerformed

    public static void main(String args[]) {

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
    private javax.swing.JTextArea textCode;
    private javax.swing.JMenuItem mArquivo;
    private javax.swing.JMenuItem mDebug;
    private javax.swing.JMenuItem mReset;
    private javax.swing.JMenuItem mExecutar;
    private javax.swing.JMenuItem mStatus;
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
    
    private class Filter extends DocumentFilter {
        private static final String PROMPT = "";
        
        private int getPromptPosition(final DocumentFilter.FilterBypass fb, final int offset){
            Document doc = fb.getDocument();
            Element root = doc.getDefaultRootElement();
            int count = root.getElementCount();
            int index = root.getElementIndex(offset);
            Element cur = root.getElement(index);
            return cur.getStartOffset()+PROMPT.length();
        }
        
        @Override
        public void insertString(final DocumentFilter.FilterBypass fb, final int offset, final String string, final AttributeSet attr)
                throws BadLocationException {
            if (offset >= getPromptPosition(fb, offset)) {
                super.insertString(fb, offset, string, attr);
            }
        }

        @Override
        public void remove(final DocumentFilter.FilterBypass fb, final int offset, final int length) throws BadLocationException {
            if (offset >= getPromptPosition(fb, offset)) {
                super.remove(fb, offset, length);
            }
        }

        @Override
        public void replace(final DocumentFilter.FilterBypass fb, final int offset, final int length, final String text, final AttributeSet attrs)
                throws BadLocationException {
            if (offset >= getPromptPosition(fb, offset)) {
                super.replace(fb, offset, length, text, attrs);
            }
        }
    }
    
    public void setTableCom(String str, int line){
        model.setValueAt(str, line, 4);
    }
    
    public String getTableInstrucoes(int line){
        return tableInstrucoes.getValueAt(line, 1).toString();
    }
    
    public int getTableParam1(int line){
        try{
        return Integer.parseInt(tableInstrucoes.getValueAt(line, 2).toString());
        }catch(NumberFormatException e){
            System.out.println("Nao tem param 1");
            return 0;
        }
    }
    
    public int getTableParam2(int line){
        try{
            return Integer.parseInt(tableInstrucoes.getValueAt(line, 3).toString());
        }catch(NumberFormatException e){
            System.out.println("Nao tem param 2");
            return 0;
        }
    }
    
    private void runCode(int state){
        interfaceVmCodigo = new InterfaceVmCodigo();
        this.state = state;
        if(this.state == RUN){
            System.out.println("runCode");
            interfaceVmCodigo.run(this);
        }
        if(this.state == RUN_DEBUG){
            System.out.println("runCodeDebug");
            InterfaceVmCodigo.setNxtInst(false);
            interfaceVmCodigo.runDebug(this, stopInstruction);
        }  
    }
    
    public void readValue(){
        mStatus.setForeground(Color.GREEN);
        mStatus.setText("Line "+(InterfaceVmCodigo.getI()));
        textTerminal.setEditable(true);
    }
    
    private void returnValueRead(){
        if (this.state == RUN) {
            System.out.println("Valor lido: " + valorLido);
            interfaceVmCodigo.setReturnedValue(this, Integer.parseInt(valorLido));
        }
        if(this.state == RUN_DEBUG){
            System.out.println("Valor lido: " + valorLido);
            interfaceVmCodigo.setReturnedValue(this, Integer.parseInt(valorLido), stopInstruction);
        }  
    }
    
    public void finishExecution(){
        if(this.state == RUN){
            mDebug.setEnabled(true);
        }
        if(this.state == RUN_DEBUG){
            mExecutar.setEnabled(true);
        }
        mStatus.setText("");
    }
    
    public void interruption(){
        stopInstruction = -1;
        mStatus.setForeground(Color.GREEN);
        mStatus.setText("Line "+(InterfaceVmCodigo.getI()));
        btnNext.setEnabled(true);
        btnRun.setEnabled(true);
    }
}
