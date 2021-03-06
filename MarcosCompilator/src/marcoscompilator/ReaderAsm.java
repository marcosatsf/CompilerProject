package marcoscompilator;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

public class ReaderAsm {

    private String path;
    private VirtualMachine vm;
    private ArrayList<IndiceMap> instructionPointer;
    private ArrayList<IndiceMap> completeLabel;
    private InterfaceVmCodigo interfaceVmCodigo;

    public ReaderAsm(String path) {
        this.path = path;
        vm = VirtualMachine.getInstance();
        instructionPointer = new ArrayList<>();
        completeLabel = new ArrayList<>();
        interfaceVmCodigo = new InterfaceVmCodigo();
        readFile();
    }

    private void readFile() {
        try {
            File c = new File(path);
            Scanner myReader = new Scanner(c);

            String data;
            String[] splitted;

            int i = 0;

            while (myReader.hasNextLine()) {
                data = myReader.nextLine();
                splitted = data.split("( )|,");

                populateTable(i, splitted);
                i++;
            }

            verifyLabels();
            interfaceVmCodigo.populateTableCom(vm);
            vm.setVisible(true);

        } catch (FileNotFoundException ex) {
            JOptionPane.showMessageDialog(vm, "Erro ao tentar abrir o arquivo.", "Ooops", JOptionPane.WARNING_MESSAGE);
        }
    }

    private void verifyLabels() {
        for (IndiceMap label : completeLabel) {           //JMP/JMPF/CALL e a label que eles pulam
            for (IndiceMap cod : instructionPointer) {    //Label e a linha que ela ta 
                if (label.getLabel().equals(cod.getLabel())) {
                    vm.editJmpValue(cod.getLinha(), label.getLinha() + 1);
                    break;
                }
            }
        }
    }

    private void populateTable(int i, String[] splitted) {
        switch (splitted.length) {
            case 1:
                vm.addAsmRow(i, splitted[0]);
                break;
            case 2:
                try {
                    vm.addAsmRow(i, splitted[0], Integer.parseInt(splitted[1]));
                } catch (NumberFormatException e) {
                    //JMP X | JMPF X | CALL X | X NULL
                    if (splitted[1].equals("NULL")) {
                        instructionPointer.add(new IndiceMap(i, splitted[0]));
                        vm.addAsmRow(i, "NULL");
                    } else {
                        completeLabel.add(new IndiceMap(i, splitted[1]));
                        vm.addAsmRow(i, splitted[0]);
                    }
                }
                break;
            case 3:
                vm.addAsmRow(i, splitted[0], Integer.parseInt(splitted[1]), Integer.parseInt(splitted[2]));
                break;
        }
    }

    class IndiceMap {

        int linha;
        String label;

        IndiceMap(int linha, String label) {
            this.linha = linha;
            this.label = label;
        }

        int getLinha() {
            return linha;
        }

        String getLabel() {
            return label;
        }
    }
}
