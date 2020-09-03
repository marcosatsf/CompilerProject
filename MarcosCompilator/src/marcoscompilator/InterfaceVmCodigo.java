package marcoscompilator;

import java.util.ArrayList;

public class InterfaceVmCodigo {

    private static int i, s;
    ArrayList<Integer> m;
    VirtualMachine vm;
    Instrucoes inst;
    static boolean lido;
    private static boolean nxtInst;

    public InterfaceVmCodigo() {
        inst = new Instrucoes();
        m = new ArrayList<>();
        i = 0;
        s = -1;
    }

    public void setReturnedValue(VirtualMachine vm, int val) {
        m.add(val);
        run(vm);
    }
    
    public void setReturnedValue(VirtualMachine vm, int val, int local) {
        m.add(val);
        runDebug(vm, local);
    }

    public void run(VirtualMachine vm) {
        int opRet;
        String instrucao;
        while (true) {
            instrucao = vm.getTableInstrucoes(i);
            System.out.println("Executando: " + instrucao);
            opRet = inst.execute(instrucao, i, s, m, vm.getTableParam1(i), vm.getTableParam2(i));

            if (opRet == Instrucoes.READ_VALUE) {
                lido = false;
                System.out.println("Pedindo pra VM LER");
                vm.readValue();
                break;
            } else if (opRet == Instrucoes.PRINT_VALUE) {
                System.out.println("Value: " + (m.get(s))); //Tem algo errado, não precisa desse -1 =
                s--;
            }
            vm.updateStack(m);
            if (vm.getTableInstrucoes(i).equals("HLT")) {
                vm.finishExecution();
                break;
            }
            InterfaceVmCodigo.setI(i+1);
        }
    }
    
    public void runDebug(VirtualMachine vm, int local) {
        int opRet;
        String instrucao;
        boolean requestStop = false;
        do{
            if(local == i){
                //requestStop = true;
                vm.interruption();
                break;
            }
            else{
                instrucao = vm.getTableInstrucoes(i);
                System.out.println("Executando: " + instrucao);
                opRet = inst.execute(instrucao, i, s, m, vm.getTableParam1(i), vm.getTableParam2(i));
                //---> 'i' is updated!
                if (opRet == Instrucoes.READ_VALUE) {
                    lido = false;
                    System.out.println("Pedindo pra VM LER");
                    vm.readValue();
                    break;
                } else if (opRet == Instrucoes.PRINT_VALUE) {
                    System.out.println("Value: " + (m.get(s))); //Tem algo errado, não precisa desse -1 =
                    s--;
                }
                vm.updateStack(m);
                if (vm.getTableInstrucoes(i).equals("HLT")) {
                    break;
                }
                InterfaceVmCodigo.setI(i+1);
                if (isNxtInst()){
                    vm.interruption();
                    break;
                }
            }
        }while (true);
    }

    public static void setLeitura(boolean x) {
        lido = x;
    }

    public static boolean getLeitura() {
        return lido;
    }

    public void populateTableCom(VirtualMachine vm) {
        String stringCom;
        for (int i = 0;; i++) {
            stringCom = inst.executeCom(vm.getTableInstrucoes(i));
            vm.setTableCom(stringCom, i);
            if (vm.getTableInstrucoes(i).equals("HLT")) {
                break;
            }
        }
    }
    
    public static void setNxtInst(boolean value){
        nxtInst = value;
    }
    
    public static boolean isNxtInst(){
        return nxtInst;
    }

    public static void setI(int newI) {
        i = newI;
    }
    
    public static int getI() {
        return i;
    }

    public static void setS(int newS) {
        s = newS;
    }
}
