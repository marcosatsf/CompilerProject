package marcoscompilator;

import java.util.ArrayList;

public class InterfaceVmCodigo {
    static int i, s;
    ArrayList<Integer> m;
    VirtualMachine vm;
    Instrucoes inst;
    static boolean lido;
    
    public InterfaceVmCodigo(){
        inst = new Instrucoes();
        m = new ArrayList<>();
        i = 0;
    }
    
    public void setReturnedValue(VirtualMachine vm, int val){
        m.add(val);
        run(vm);
    }
    
    public void run(VirtualMachine vm){
        int opRet;
        String instrucao;
        while(true){
            instrucao = vm.getTableInstrucoes(i);
            System.out.println("Executando: " + instrucao);
            opRet = inst.execute(instrucao, i, s, m, vm.getTableParam1(i), vm.getTableParam2(i));
            
            if(opRet == Instrucoes.READ_VALUE) {
                lido = false;
                System.out.println("Pedindo pra VM LER");
                vm.readValue();
                break;
            }
            else if(opRet == Instrucoes.PRINT_VALUE) {
                System.out.println("Value: " + (m.get(s))); //Tem algo errado, não precisa desse -1 =
                s++;
            }
            if(vm.getTableInstrucoes(i).equals("HLT")) break;
        }
    }
    
    public static void setLeitura(boolean x){
        lido = x;
    }
    public static boolean getLeitura(){
        return lido;
    }
    
    public void populateTableCom(VirtualMachine vm){
        String stringCom;
        for(int i=0;;i++){
            stringCom = inst.executeCom(vm.getTableInstrucoes(i));
            vm.setTableCom(stringCom, i);
            if(vm.getTableInstrucoes(i).equals("HLT")) break;
        }
    }
    
    public static void setI(int newI){
        i = newI;
    }
    
    public static void setS(int newS){
        s = newS;
    }
}
