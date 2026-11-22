package com.seer.template;

import android.app.Activity;
import android.os.Build;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        TextView tv = new TextView(this);
        tv.setText(getString(R.string.seer_text) + "\n" + Build.MODEL);
        tv.setTextSize(24);
        tv.setGravity(android.view.Gravity.CENTER);
        setContentView(tv);
    }
}
