package marcoscompilator;

import java.util.ArrayList;

public class Instrucoes {
    public void execute(String comando, int i, int s, ArrayList<Integer> m,
            int param1, int param2)
    {
        switch(comando)
        {
            case "LDC":
                LDC(param1, s, m);
                break;
            case "LDV":
                LDV(param1, s, m);
                break;
            case "ADD":
                ADD(s, m);
                break;
            case "SUB":
                SUB(s, m);
                break;
            case "MULT":
                MULT(s, m);
                break;
            case "DIVI":
                DIVI(s, m);
                break;
            case "INV":
                INV(s, m);
                break;
            case "AND":
                AND(s, m);
                break;
            case "OR":
                OR(s, m);
                break;
            case "NEG":
                NEG(s, m);
                break;
            case "CME":
                CME(s, m);
                break;
            case "CMA":
                CMA(s, m);
                break;
            case "CEQ":
                CEQ(s, m);
                break;
            case "CDIF":
                CDIF(s, m);
                break;
            case "CMEQ":
                CMEQ(s, m);
                break;
            case "CMAQ":
                CMAQ(s, m);
                break;
            case "START":
                
                break;
            case "HLT":
                
                break;
            case "STR":
                STR(param1, s, m);
                break;
            case "JMP":
                JMP(s, i);
                break;
            case "JMPF":
                JMPF(param1, i, s, m);
                break;
            case "NULL":
                break;
            case "RD":
                RD(param1, i, s, m);
                break;
            case "PRN":
                PRN(s, m);
                break;
            case "ALLOC":
                ALLOC(param1, param2, s, m);
                break;
            case "DALLOC":
                DALLOC(param1, param2, s, m);
                break;
            case "CALL":
                CALL(param1, i, s, m);
                break;
            case "RETURN":
                RETURN(i, s, m);
                break;
        }
    }
    
    public void executeComcom(String comando)
    {
        switch(comando)
        {
            case "LDC":
                LDCcom();
                break;
            case "LDV":
                LDVcom();
                break;
            case "ADD":
                ADDcom();
                break;
            case "SUB":
                SUBcom();
                break;
            case "MULT":
                MULTcom();
                break;
            case "DIVI":
                DIVIcom();
                break;
            case "INV":
                INVcom();
                break;
            case "AND":
                ANDcom();
                break;
            case "OR":
                ORcom();
                break;
            case "NEG":
                NEGcom();
                break;
            case "CME":
                CMEcom();
                break;
            case "CMA":
                CMAcom();
                break;
            case "CEQ":
                CEQcom();
                break;
            case "CDIF":
                CDIFcom();
                break;
            case "CMEQ":
                CMEQcom();
                break;
            case "CMAQ":
                CMAQcom();
                break;
            case "START":
                STARTcom();
                break;
            case "HLT":
                HLTcom();
                break;
            case "STR":
                STRcom();
                break;
            case "JMP":
                JMPcom();
                break;
            case "JMPF":
                JMPFcom();
                break;
            case "NULL":
                break;
            case "RD":
                RDcom();
                break;
            case "PRN":
                PRNcom();
                break;
            case "ALLOC":
                ALLOCcom();
                break;
            case "DALLOC":
                DALLOCcom();
                break;
            case "CALL":
                CALLcom();
                break;
            case "RETURN":
                RETURNcom();
                break;
        }
    }
    
    //LDC k (Carregar constante), S:=s + 1 ; M [s]: = k 
    private void LDC(int p1, int s, ArrayList<Integer> m){
        s++;
        m.add(s, p1);
    }
    private String LDCcom(){
        return "S:=s + 1 ; M [s]: = Param#1";
    }
    //LDV n (Carregar valor), S:=s + 1 ; M[s]:=M[n] 
    private void LDV(int p1, int s, ArrayList<Integer> m){
        s++;
        m.add(s, m.get(p1));
    }
    private String LDVcom(){
        return "S:=s + 1 ; M[s]:=M[Param#1]";
    }
    //ADD (Somar), M[s-1]:=M[s-1] + M[s]; s:=s - 1
    private void ADD(int s, ArrayList<Integer> m){
        m.add(s-1, m.get(s-1)+m.get(s));
        s--;
    }
    private String ADDcom(){
        return "M[s-1]:=M[s-1] + M[s]; s:=s - 1";
    }
    //SUB (Subtrair), M[s-1]:=M[s-1] - M[s]; s:=s - 1
    private void SUB(int s, ArrayList<Integer> m){
        m.add(s-1, m.get(s-1)-m.get(s));
        s--;
    }
    private String SUBcom(){
        return "M[s-1]:=M[s-1] - M[s]; s:=s - 1";
    }
    //MULT (Multiplicar), M[s-1]:=M[s-1] * M[s]; s:=s - 1
    private void MULT(int s, ArrayList<Integer> m){
        m.add(s-1, m.get(s-1)*m.get(s));
        s--;
    }
    private String MULTcom(){
        return "M[s-1]:=M[s-1] * M[s]; s:=s - 1";
    }
    //DIVI (Dividir), M[s-1]:=M[s-1] div M[s]; s:=s - 1
    private void DIVI(int s, ArrayList<Integer> m){
        m.add(s-1, m.get(s-1)/m.get(s));
        s--;
    }
    private String DIVIcom(){
        return "M[s-1]:=M[s-1] div M[s]; s:=s - 1";
    }
    //INV (Inverter sinal), M[s]:= -M[s]
    private void INV(int s, ArrayList<Integer> m){
        m.add(s, -m.get(s));
    }
    private String INVcom(){
        return "M[s]:= -M[s]";
    }
    /*AND (Conjunção), 
    se M [s-1] = 1 e M[s] = 1 então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private void AND(int s, ArrayList<Integer> m){
        if(m.get(s-1) == 1 && m.get(s) == 1) m.add(s-1, 1);
        else m.add(s-1, 0);
        s--;
    }
    private String ANDcom(){
        return "se M [s-1] = 1 e M[s] = 1 então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*OR (Disjunção),
    se M[s-1] = 1 ou M[s] = 1 então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private void OR(int s, ArrayList<Integer> m){
        if(m.get(s-1) == 1 || m.get(s) == 1) m.add(s-1, 1);
        else m.add(s-1, 0);
        s--;
    }
    private String ORcom(){
        return "se M[s-1] = 1 ou M[s] = 1 então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    //NEG (Negação), M[s]:=1 - M[s]
    private void NEG(int s, ArrayList<Integer> m){
        m.add(s, 1-m.get(s));
    }
    private String NEGcom(){
        return "M[s]:=1 - M[s]";
    }
    /*CME (Comparar menor):
    se M[s-1] < M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private void CME(int s, ArrayList<Integer> m){
        if(m.get(s-1) < m.get(s)) m.add(s-1, 1);
        else m.add(s-1, 0);
        s--;
    }
    private String CMEcom(){
        return "se M[s-1] < M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*CMA (Comparar maior):
    se M[s-1] > M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private void CMA(int s, ArrayList<Integer> m){
        if(m.get(s-1) > m.get(s)) m.add(s-1, 1);
        else m.add(s-1, 0);
        s--;
    }
    private String CMAcom(){
        return "se M[s-1] > M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*CEQ (Comparar igual):
    se M[s-1] = M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private void CEQ(int s, ArrayList<Integer> m){
        if(m.get(s-1) == m.get(s)) m.add(s-1, 1);
        else m.add(s-1, 0);
        s--;
    }
    private String CEQcom(){
        return "se M[s-1] = M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*CDIF (Comparar desigual):
    se M[s-1] ≠ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private void CDIF(int s, ArrayList<Integer> m){
        if(m.get(s-1) != m.get(s)) m.add(s-1, 1);
        else m.add(s-1, 0);
        s--;
    }
    private String CDIFcom(){
        return "se M[s-1] ≠ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*CMEQ (Comparar menor ou igual)
    se M[s-1] ≤ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private void CMEQ(int s, ArrayList<Integer> m){
        if(m.get(s-1) <= m.get(s)) m.add(s-1, 1);
        else m.add(s-1, 0);
        s--;
    }
    private String CMEQcom(){
        return "se M[s-1] ≤ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    /*CMAQ (Comparar maior ou igual):
    se M[s-1] ≥ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1
    */
    private void CMAQ(int s, ArrayList<Integer> m){
        if(m.get(s-1) >= m.get(s)) m.add(s-1, 1);
        else m.add(s-1, 0);
        s--;
    }
    private String CMAQcom(){
        return "se M[s-1] ≥ M[s] então M[s-1]:=1 senão M[s-1]:=0; s:=s - 1";
    }
    //START (Iniciar programa principal), S:=-1
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
    private void STR(int p1, int s, ArrayList<Integer> m){
        m.add(p1, m.get(s));
        s--;
    }
    private String STRcom(){
        return "M[Param#1]:=M[s]; s:=s-1";
    }
    //Desvios (não há o incremento implícito sobre i)
    //JMP t (Desviar sempre), i:= t
    private void JMP(int p1, int i){
        i = p1;
    }
    private String JMPcom(){
        return "i:= Param#1";
    }
    /*JMPF t (Desviar se falso)
    se M[s] = 0 então i:=t senão i:=i + 1; s:=s-1
    */
    private void JMPF(int p1, int i, int s, ArrayList<Integer> m){
        if(m.get(s) == 0) i = p1;
        else i++;
        s--;
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
    private void RD(int p1, int i, int s, ArrayList<Integer> m){
        s++;
        //TODO m.add(s, );
    }
    private String RDcom(){
        return "S:=s + 1; M[s]:= “próximo valor de entrada”.";
    }
    //Saída
    //PRN (Impressão), “Imprimir M[s]”; s:=s-1
    private int PRN(int s, ArrayList<Integer> m){
        return m.get(--s);
        //TODO m.add(s, );
    }
    private String PRNcom(){
        return "“Imprimir M[s]”; s:=s-1";
    }
    //Alocação e Desalocação de Variáveis
    /*ALLOC m,n (Alocar memória)
    Para k:=0 até n-1 faça
    {s:=s + 1; M[s]:=M[m+k]}
    */
    private void ALLOC(int p1, int p2, int s, ArrayList<Integer> m){
        for(int k = 0; k < p2; k++){
            s++;
            m.add(s, m.get(p1+k));
        }
    }
    private String ALLOCcom(){
        return "Para k:=0 até Param#2-1 faça -> {s:=s + 1; M[s]:=M[Param#1+k]}";
    }
    /*DALLOC m,n (Desalocar memória):
    Para k:=n-1 até 0 faça
    {M[m+k]:=M[s]; s:=s - 1}
    */
    private void DALLOC(int p1, int p2, int s, ArrayList<Integer> m){
        for(int k = p2-1; k >= 0; k--){
            m.add(p1+k, m.get(s));
            s--;
        }
    }
    private String DALLOCcom(){
        return "Para k:=Param#2-1 até 0 faça -> {M[Param#1+k]:=M[s]; s:=s - 1}";
    }
    //Chamada de Rotina
    //CALL t (Chamar procedimento ou função), S:=s + 1; M[s]:=i + 1; i:=t
    private void CALL(int p1, int i, int s, ArrayList<Integer> m){
        s++;
        m.add(s, i+1);
        i = p1;
    }
    private String CALLcom(){
        return "S:=s + 1; M[s]:=i + 1; i:=Param#1";
    }
    //RETURN (Retornar de procedimento), i:=M[s]; s:=s - 1
    private void RETURN(int i, int s, ArrayList<Integer> m){
        i = m.get(s);
        s--;
    }
    private String RETURNcom(){
        return "i:=M[s]; s:=s - 1";
    }
}
