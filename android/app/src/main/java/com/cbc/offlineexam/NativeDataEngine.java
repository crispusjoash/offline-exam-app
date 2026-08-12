package com.cbc.offlineexam;

import android.content.res.AssetManager;
import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

@CapacitorPlugin(name = "NativeData")
public class NativeDataEngine extends Plugin {

    @PluginMethod
    public void getPaper(PluginCall call) {
        String fileName = call.getString("file");
        if (fileName == null) {
            call.reject("Must provide a file name");
            return;
        }

        try {
            AssetManager assetManager = getContext().getAssets();
            // Capacitor places web assets in public/
            InputStream inputStream = assetManager.open("public/data/" + fileName);
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8));
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                sb.append(line);
            }
            reader.close();

            JSObject ret = new JSObject();
            ret.put("data", sb.toString());
            call.resolve(ret);
        } catch (Exception e) {
            call.reject("Failed to read " + fileName + ": " + e.getMessage(), e);
        }
    }
}
