package marcoscompilator;

import java.util.ArrayList;

public class InterfaceVmCodigo {
    int i, s;
    ArrayList<Integer> m;
    VirtualMachine vm;
    Instrucoes inst;
    
    public InterfaceVmCodigo(){
        inst = new Instrucoes();
        m = new ArrayList<>();
        i = 0;
    }
    
    public void run(VirtualMachine vm){
        int opRet;
        while(true){
            opRet = inst.execute(vm.getTableInstrucoes(i), i, s, m, vm.getTableParam1(i), vm.getTableParam2(i));
            if(opRet == Instrucoes.READ_VALUE) {
                vm.readValue();
            }
//            else if(opRet == Instrucoes.PRINT_VALUE) {
//                vm.
//            }
//            vm.setTableCom(stringCom, i);
            if(vm.getTableInstrucoes(i).equals("HLT")) break;
        }
    }
    
    public void populateTableCom(VirtualMachine vm){
        String stringCom;
        for(int i=0;;i++){
            stringCom = inst.executeCom(vm.getTableInstrucoes(i));
            vm.setTableCom(stringCom, i);
            if(vm.getTableInstrucoes(i).equals("HLT")) break;
        }
    }
}
