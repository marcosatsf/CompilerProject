package marcoscompilator;

import java.util.ArrayList;

public class Instrucoes {
    public static final int DEFAULT_VALUE = 0;
    public static final int READ_VALUE = 1;
    public static final int PRINT_VALUE = 2;
    public static final int ERROR_VALUE = -1;
    
    
    public int execute(String comando, int i, int s, ArrayList<Integer> m,
            int param1, int param2)
    {
        InterfaceVmCodigo.setI(++i);
        switch(comando)
        {
            case "LDC":
                return LDC(param1, s, m);
            case "LDV":
                return LDV(param1, s, m);
            case "ADD":
                return ADD(s, m);
            case "SUB":
                return SUB(s, m);
            case "MULT":
                return MULT(s, m);
            case "DIVI":
                return DIVI(s, m);
            case "INV":
                return INV(s, m);
            case "AND":
                return AND(s, m);
            case "OR":
                return OR(s, m);
            case "NEG":
                return NEG(s, m);
            case "CME":
                return CME(s, m);
            case "CMA":
                return CMA(s, m);
            case "CEQ":
                return CEQ(s, m);
            case "CDIF":
                return CDIF(s, m);
            case "CMEQ":
                return CMEQ(s, m);
            case "CMAQ":
                return CMAQ(s, m);
            case "START":
                return START();
            case "HLT":
                return DEFAULT_VALUE;
            case "STR":
                return STR(param1, s, m);
            case "JMP":
                return JMP(s, i);
            case "JMPF":
                return JMPF(param1, i, s, m);
            case "NULL":
                break;
            case "RD":
                return RD(param1, s, m);
            case "PRN":
                return PRN(s);
            case "ALLOC":
                return ALLOC(param1, param2, s, m);
            case "DALLOC":
                return DALLOC(param1, param2, s, m);
            case "CALL":
                return CALL(param1, i, s, m);
            case "RETURN":
                return RETURN(i, s, m);
        }
        return ERROR_VALUE;
    }
    
    public String executeCom(String comando)
    {
        switch(comando)
        {
            case "LDC":
                return LDCcom();
            case "LDV":
                return LDVcom();
            case "ADD":
                return ADDcom();
            case "SUB":
                return SUBcom();
            case "MULT":
                return MULTcom();
            case "DIVI":
                return DIVIcom();
            case "INV":
                return INVcom();
            case "AND":
                return ANDcom();
            case "OR":
                return ORcom();
            case "NEG":
                return NEGcom();
            case "CME":
                return CMEcom();
            case "CMA":
                return CMAcom();
            case "CEQ":
                return CEQcom();
            case "CDIF":
                return CDIFcom();
            case "CMEQ":
                return CMEQcom();
            case "CMAQ":
                return CMAQcom();
            case "START":
                return STARTcom();
            case "HLT":
                return HLTcom();
            case "STR":
                return STRcom();
            case "JMP":
                return JMPcom();
            case "JMPF":
                return JMPFcom();
            case "NULL":
                return "";
            case "RD":
                return RDcom();
            case "PRN":
                return PRNcom();
            case "ALLOC":
                return ALLOCcom();
            case "DALLOC":
                return DALLOCcom();
            case "CALL":
                return CALLcom();
            case "RETURN":
                return RETURNcom();
        }
        return "";
    }
    
    //LDC k (Carregar constante), S:=s + 1 ; M [s]: = k 
    private int LDC(int p1, int s, ArrayList<Integer> m){
        InterfaceVmCodigo.setS(++s);
        m.set(s, p1);
        return DEFAULT_VALUE;
    }
    private String LDCcom(){
        return "S:=s + 1 ; M [s]: = Param#1";
    }
    //LDV n (Carregar valor), S:=s + 1 ; M[s]:=M[n] 
    private int LDV(int p1, int s, ArrayList<Integer> m){
        InterfaceVmCodigo.setS(++s);
        m.set(s, m.get(p1));
        return DEFAULT_VALUE;
    }
    private String LDVcom(){
        return "S:=s + 1 ; M[s]:=M[Param#1]";
    }
    //ADD (Somar), M[s-1]:=M[s-1] + M[s]; s:=s - 1
    private int ADD(int s, ArrayList<Integer> m){
        int sum = m.get(s-1) + m.get(s);
        m.set((s-1), sum);
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String ADDcom(){
        return "M[s-1]:=M[s-1] + M[s]; s:=s - 1";
    }
    //SUB (Subtrair), M[s-1]:=M[s-1] - M[s]; s:=s - 1
    private int SUB(int s, ArrayList<Integer> m){
        m.set(s-1, m.get(s-1)-m.get(s));
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String SUBcom(){
        return "M[s-1]:=M[s-1] - M[s]; s:=s - 1";
    }
    //MULT (Multiplicar), M[s-1]:=M[s-1] * M[s]; s:=s - 1
    private int MULT(int s, ArrayList<Integer> m){
        m.set(s-1, m.get(s-1)*m.get(s));
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String MULTcom(){
        return "M[s-1]:=M[s-1] * M[s]; s:=s - 1";
    }
    //DIVI (Dividir), M[s-1]:=M[s-1] div M[s]; s:=s - 1
    private int DIVI(int s, ArrayList<Integer> m){
        m.set(s-1, m.get(s-1)/m.get(s));
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String DIVIcom(){
        return "M[s-1]:=M[s-1] div M[s]; s:=s - 1";
    }
    //INV (Inverter sinal), M[s]:= -M[s]
    private int INV(int s, ArrayList<Integer> m){
        m.set(s, -m.get(s));
        return DEFAULT_VALUE;
    }
    private String INVcom(){
        return "M[s]:= -M[s]";
    }
    /*AND (Conjunção), 
    se M [s-1] = 1 e M[s] = 1 então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private int AND(int s, ArrayList<Integer> m){
        if(m.get(s-1) == 1 && m.get(s) == 1) m.set(s-1, 1);
        else m.set(s-1, 0);
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String ANDcom(){
        return "se M [s-1] = 1 e M[s] = 1 então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*OR (Disjunção),
    se M[s-1] = 1 ou M[s] = 1 então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private int OR(int s, ArrayList<Integer> m){
        if(m.get(s-1) == 1 || m.get(s) == 1) m.set(s-1, 1);
        else m.set(s-1, 0);
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String ORcom(){
        return "se M[s-1] = 1 ou M[s] = 1 então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    //NEG (Negação), M[s]:=1 - M[s]
    private int NEG(int s, ArrayList<Integer> m){
        m.set(s, 1-m.get(s));
        return DEFAULT_VALUE;
    }
    private String NEGcom(){
        return "M[s]:=1 - M[s]";
    }
    /*CME (Comparar menor):
    se M[s-1] < M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private int CME(int s, ArrayList<Integer> m){
        if(m.get(s-1) < m.get(s)) m.set(s-1, 1);
        else m.set(s-1, 0);
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String CMEcom(){
        return "se M[s-1] < M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*CMA (Comparar maior):
    se M[s-1] > M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private int CMA(int s, ArrayList<Integer> m){
        if(m.get(s-1) > m.get(s)) m.set(s-1, 1);
        else m.set(s-1, 0);
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String CMAcom(){
        return "se M[s-1] > M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*CEQ (Comparar igual):
    se M[s-1] = M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private int CEQ(int s, ArrayList<Integer> m){
        if(m.get(s-1) == m.get(s)) m.set(s-1, 1);
        else m.set(s-1, 0);
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String CEQcom(){
        return "se M[s-1] = M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*CDIF (Comparar desigual):
    se M[s-1] ≠ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private int CDIF(int s, ArrayList<Integer> m){
        if(m.get(s-1) != m.get(s)) m.set(s-1, 1);
        else m.set(s-1, 0);
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String CDIFcom(){
        return "se M[s-1] ≠ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*CMEQ (Comparar menor ou igual)
    se M[s-1] ≤ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private int CMEQ(int s, ArrayList<Integer> m){
        if(m.get(s-1) <= m.get(s)) m.set(s-1, 1);
        else m.set(s-1, 0);
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String CMEQcom(){
        return "se M[s-1] ≤ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*CMAQ (Comparar maior ou igual):
    se M[s-1] ≥ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private int CMAQ(int s, ArrayList<Integer> m){
        if(m.get(s-1) >= m.get(s)) m.set(s-1, 1);
        else m.set(s-1, 0);
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String CMAQcom(){
        return "se M[s-1] ≥ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    //START (Iniciar programa principal), S:=-1
    private int START(){
        InterfaceVmCodigo.setS(-1);
        return DEFAULT_VALUE;
    }
    private String STARTcom(){
        return "(Iniciar programa principal), S:=-1";
    }
    //private void START(int s){s--;}
    //HLT (Parar), “Pára a execução da MVD”
    private String HLTcom(){
        return "(Parar), “Pára a execução da MVD”";
    }
    //
    //STR n (Armazenar valor), M[n]:=M[s]; s:=s-1
    private int STR(int p1, int s, ArrayList<Integer> m){
        m.set(p1, m.get(s));
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String STRcom(){
        return "M[Param#1]:=M[s]; s:=s-1";
    }
    //Desvios (não há o incremento implícito sobre i)
    //JMP t (Desviar sempre), i:= t
    private int JMP(int p1, int i){
        InterfaceVmCodigo.setI(p1);
        return DEFAULT_VALUE;
    }
    private String JMPcom(){
        return "i:= Param#1";
    }
    /*JMPF t (Desviar se falso)
    se M[s] = 0 então i:=t senão i:=i + 1; s:=s-1
    */
    private int JMPF(int p1, int i, int s, ArrayList<Integer> m){
        if(m.get(s) == 0) 
            InterfaceVmCodigo.setI(p1);
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String JMPFcom(){
        return "se M[s] = 0 então i:=Param#1 senão i:=i + 1; s:=s-1";
    }
    //Operação Nula
    //NULL (Nada)
    
    //Entrada
    //TODO
    /*RD (Leitura):
    S:=s + 1; M[s]:= “próximo valor de entrada”.
    */
    private int RD(int p1, int s, ArrayList<Integer> m){
        InterfaceVmCodigo.setS(++s);
        return READ_VALUE;
        //TODO m.set(s, );
    }
    private String RDcom(){
        return "S:=s + 1; M[s]:= “próximo valor de entrada”.";
    }
    //Saída
    //PRN (Impressão), “Imprimir M[s]”; s:=s-1
    private int PRN(int s){
        return PRINT_VALUE;
        //TODO m.set(s, );
    }
    private String PRNcom(){
        return "“Imprimir M[s]”; s:=s-1";
    }
    //Alocação e Desalocação de Variáveis
    /*ALLOC m,n (Alocar memória)
    Para k:=0 até n-1 faça
    {s:=s + 1; M[s]:=M[m+k]}
    *///TODO popular o m com lixoooooooooooooooooooo
    private int ALLOC(int p1, int p2, int s, ArrayList<Integer> m){
        for(int k = 0; k < p2; k++){
            InterfaceVmCodigo.setS(++s);
            m.set(s, m.get(p1+k));
        }
        return DEFAULT_VALUE;
    }
    private String ALLOCcom(){
        return "Para k:=0 até Param#2-1 faça -> {s:=s + 1; M[s]:=M[Param#1+k]}";
    }
    /*DALLOC m,n (Desalocar memória):
    Para k:=n-1 até 0 faça
    {M[m+k]:=M[s]; s:=s - 1}
    */
    private int DALLOC(int p1, int p2, int s, ArrayList<Integer> m){
        for(int k = p2-1; k >= 0; k--){
            m.set(p1+k, m.get(s));
            InterfaceVmCodigo.setS(--s);
        }
        return DEFAULT_VALUE;
    }
    private String DALLOCcom(){
        return "Para k:=Param#2-1 até 0 faça -> {M[Param#1+k]:=M[s]; s:=s - 1}";
    }
    //Chamada de Rotina
    //CALL t (Chamar procedimento ou função), S:=s + 1; M[s]:=i + 1; i:=t
    private int CALL(int p1, int i, int s, ArrayList<Integer> m){
        InterfaceVmCodigo.setS(++s);
        m.set(s, i);
        InterfaceVmCodigo.setI(p1);
        return DEFAULT_VALUE;
    }
    private String CALLcom(){
        return "S:=s + 1; M[s]:=i + 1; i:=Param#1";
    }
    //RETURN (Retornar de procedimento), i:=M[s]; s:=s - 1
    private int RETURN(int i, int s, ArrayList<Integer> m){
        InterfaceVmCodigo.setI(m.get(s));
        InterfaceVmCodigo.setS(--s);
        return DEFAULT_VALUE;
    }
    private String RETURNcom(){
        return "i:=M[s]; s:=s - 1";
    }
}
