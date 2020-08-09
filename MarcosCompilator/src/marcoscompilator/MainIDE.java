package marcoscompilator;

import java.awt.FileDialog;
import java.awt.Frame;

public class MainIDE {

    private static MainIDE instance = null;
    
    public static MainIDE getInstance(){
        if(instance == null)
            instance = new MainIDE();
        return instance;
    }
    
    public static void main(String[] args) {
        StartScreen startScreen = new StartScreen();
        startScreen.setVisible(true);
    }
    
    public void startSobreNosScreen(){
        SobreNosScreen sns = new SobreNosScreen();
        sns.setVisible(true);
    }
    
    public void startVirtualMachine(){
        VirtualMachine vm = new VirtualMachine();
        vm.setVisible(true);
    }
    
    public void loadCode(){
        FileDialog dialog = new FileDialog((Frame)null, "Select File to Open");
        dialog.setMode(FileDialog.LOAD);
        dialog.setFile("*.baz;*.c;*.asm");
        dialog.setVisible(true);
        
        String path = dialog.getDirectory() + dialog.getFile();
        System.out.println(path);
        
        ReaderAsm reader = new ReaderAsm(path);
    }
}
