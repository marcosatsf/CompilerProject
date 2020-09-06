package marcoscompilator;

import java.util.ArrayList;

public class InterfaceVmCodigo {

    static int i, s;
    ArrayList<Integer> m;
    VirtualMachine vm;
    Instrucoes inst;
    static boolean lido;
    boolean isRun;

    public InterfaceVmCodigo() {
        inst = new Instrucoes();
        m = new ArrayList<>();
        i = 0;
    }

    public void setReturnedValue(VirtualMachine vm, int val, boolean isDebug, ArrayList<Integer> breakPoints) {
        m.add(val);
        run(vm, isDebug, breakPoints);
    }

    public void run(VirtualMachine vm, boolean isDebug, ArrayList<Integer> breakPoints) {
        int opRet;
        String instrucao;
        int param1;
        int param2;
        while (true) {
            
            if(isDebug){
                if(isRun){
                    if(breakPoints.contains(i)){
                        isRun = false;
                        vm.updateStack(m);
                        System.out.println("Breikei");
                        break;
                    }
                }
            }
            
            instrucao = vm.getTableInstrucoes(i);
            param1 = vm.getTableParam1(i);
            param2 = vm.getTableParam2(i);
            
            System.out.println("Valores: i: " + i + " s: " + s);
            System.out.println("Instrucao que sera executada: " + 
                        instrucao + 
                            " " + param1 +
                                " " + param2);

            opRet = inst.execute(instrucao, i, s, m, param1, param2);

            if(opRet != Instrucoes.MOVE_I)
                i += 1;
            
            if (opRet == Instrucoes.READ_VALUE) {
                lido = false;
                System.out.println("Pedindo pra VM LER");
                vm.readValue();
                break;
            } else if (opRet == Instrucoes.PRINT_VALUE) {
                System.out.println("Pedindo pra VM PRINTAR");
                vm.printValue(m.get(s));
                s--;
            } else if (opRet == Instrucoes.MOVE_I){
                System.out.println("Move I");
            }
            
            vm.updateStack(m);
            
            if(!isRun)
                break;
            
            if (vm.getTableInstrucoes(i).equals("HLT")) {
                break;
            }     
        }
    }

    public void setIsRun(boolean x){
        isRun = x;
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

    public static void setI(int newI) {
        i = newI;
    }

    public static void setS(int newS) {
        s = newS;
    }
}
