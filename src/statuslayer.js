var StatusLayer = cc.Layer.extend({
    labelScore:null,
    score:0,

    ctor:function () {
        this._super();
        this.init();
    },

    init:function () {
        this._super();
        var winsize = cc.director.getWinSize();
        this.labelScore = new cc.LabelTTF("0", "Helvetica", 15);
        this.labelScore.setColor(cc.color(0,0,0));
        this.labelScore.setPosition(cc.p(75, winsize.height - 20));
        this.addChild(this.labelScore);

    },
    addScore:function (num) {
        this.score += num;
        if(this.score < 4) {
            this.labelScore.setString(this.score);
            return false;
        } else {
            this.labelScore.setString("You win");
            this.labelScore.setColor(cc.color(0,0,0));
            cc.director.pause();
            return true;
        }
    },
    gameOver:function() {
        this.labelScore.setString("Game over");
        this.labelScore.setColor(cc.color(0,0,0));
        cc.director.pause();
    }
});