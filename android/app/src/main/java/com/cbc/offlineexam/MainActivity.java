package com.cbc.offlineexam;

import android.os.Bundle;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        registerPlugin(NativeDataEngine.class);
        super.onCreate(savedInstanceState);
    }
}
